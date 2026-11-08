#!/usr/bin/env python3
"""ChainSentry Academy Certification Service - end-to-end.
FastAPI + SQLite registry. Issues credentials, verifies them, serves the Academy pages.
Endpoints:
  POST /api/v1/issue          {course, holder, email}      -> credential ID + PDF-ready record
  GET  /api/v1/verify/{id}                                  -> registry verdict (JSON)
  GET  /api/v1/credential/{id}                             -> full record
  GET  /api/v1/registry                                    -> all credentials
  GET  /health                                             -> liveness + db state
  /                                          -> Academy hub (index)
  /courses/{code}                            -> course pages
  /verify                                    -> verify UI (live against this API)
"""
import sqlite3, json, os, datetime, hmac, hashlib, secrets, re
from pathlib import Path

try:
    from fastapi import FastAPI, HTTPException
    from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse
    from pydantic import BaseModel, Field
    import uvicorn
except ImportError:
    raise SystemExit("fastapi/uvicorn/pydantic required")

APP_DIR = Path(__file__).parent
DESIGN = APP_DIR / "design"
DB_PATH = Path(os.environ.get("CCA_DB", "/data/registry.db"))

COURSES = {
    "BTE": "Blockchain Tracing Essentials",
    "DLF": "Digital Ledger Foundations",
    "CAP": "Certified AML Practitioner",
    "CCC": "Certified Crypto Compliance Analyst",
    "CTX": "Crypto Trace Examiner",
    "MTX": "Mixed-Chain Trace Examiner",
}
VALIDITY_DAYS = {"BTE": 730, "DLF": 0, "CAP": 730, "CCC": 730, "CTX": 730, "MTX": 730}  # 0 = lifetime
PASS_SECRETS = os.environ.get("CCA_SECRET", "dev-secret-change-me")

app = FastAPI(title="ChainSentry Academy Certification", version="1.0.0")

def db():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    c = sqlite3.connect(DB_PATH)
    c.row_factory = sqlite3.Row
    c.execute("""CREATE TABLE IF NOT EXISTS credentials (
        id TEXT PRIMARY KEY, course_code TEXT NOT NULL, course TEXT NOT NULL,
        holder TEXT NOT NULL, email TEXT,
        issued TEXT NOT NULL, expires TEXT, status TEXT NOT NULL DEFAULT 'VALID',
        serial TEXT NOT NULL, revoked_reason TEXT,
        created_at TEXT NOT NULL)""")
    c.execute("""CREATE TABLE IF NOT EXISTS exams (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        credential_id TEXT, course_code TEXT NOT NULL, candidate TEXT NOT NULL,
        started_at TEXT NOT NULL, submitted_at TEXT, score INTEGER,
        pass_mark INTEGER NOT NULL DEFAULT 70, status TEXT NOT NULL DEFAULT 'in_progress')""")
    return c

def serial_for(code: str) -> str:
    return f"{datetime.datetime.now(datetime.timezone.utc).strftime('%y%m')}-{secrets.token_hex(4).upper()}"

def next_number(c, code: str) -> int:
    row = c.execute("SELECT COUNT(*) AS n FROM credentials WHERE course_code=?", (code,)).fetchone()
    return row["n"] + 1

def cred_id(code: str, num: int) -> str:
    return f"CCA-{code}-{datetime.datetime.now(datetime.timezone.utc).year}-{num:04d}"

class IssueReq(BaseModel):
    course_code: str = Field(..., description="BTE|DLF|CAP|CCC|CTX|MTX")
    holder: str
    email: str | None = None

@app.get("/health")
def health():
    c = db()
    n = c.execute("SELECT COUNT(*) AS n FROM credentials").fetchone()["n"]
    return {"status": "ok", "service": "cca-certification", "version": "1.0.0",
            "registry_size": n, "db": str(DB_PATH), "time": datetime.datetime.now(datetime.timezone.utc).isoformat()}

@app.post("/api/v1/issue")
def issue(req: IssueReq):  # noqa
    code = req.course_code.upper()
    if code not in COURSES:
        raise HTTPException(400, f"Unknown course code {code}. Valid: {sorted(COURSES)}")
    if not req.holder or len(req.holder) < 2:
        raise HTTPException(422, "holder name required")
    c = db()
    num = next_number(c, code)
    cid = cred_id(code, num)
    now = datetime.datetime.now(datetime.timezone.utc)
    vd = VALIDITY_DAYS[code]
    expires: str | None = (now + datetime.timedelta(days=vd)).date().isoformat() if vd else None
    serial = serial_for(code)
    sig = hmac.new(PASS_SECRETS.encode(), f"{cid}|{serial}|{req.holder}".encode(), hashlib.sha256).hexdigest()[:16]
    c.execute("INSERT INTO credentials VALUES (?,?,?,?,?,?,?,?,?,?,?)",
              (cid, code, COURSES[code], req.holder, req.email,
               now.date().isoformat(), expires, "VALID", serial,
               None, now.isoformat(timespec="seconds")))
    c.commit()
    row = c.execute("SELECT * FROM credentials WHERE id=?", (cid,)).fetchone()
    return {"issued": True, "credential": dict(row), "verification_signature": sig,
            "verify_url": f"/api/v1/verify/{cid}"}

@app.get("/api/v1/verify/{cid}")
def verify(cid: str):
    c = db()
    row = c.execute("SELECT * FROM credentials WHERE UPPER(id)=UPPER(?)", (cid,)).fetchone()
    if not row:
        return {"found": False, "id": cid.upper(),
                "verdict": "NOT_FOUND",
                "note": "No credential with this ID in the registry. Check the ID and try again."}
    d = dict(row)
    if d["expires"] and d["expires"] < datetime.date.today().isoformat() and d["status"] == "VALID":
        c.execute("UPDATE credentials SET status='EXPIRED' WHERE id=?", (d["id"],)); c.commit()
        d["status"] = "EXPIRED"
    return {"found": True, **d,
            "verdict": d["status"],
            "course_title": COURSES.get(d["course_code"], d["course"])}

@app.get("/api/v1/credential/{cid}")
def credential(cid: str):
    r = verify(cid)
    if not r.get("found"):
        raise HTTPException(404, r["note"])
    return r

@app.get("/api/v1/registry")
def registry(status: str = None):
    c = db()
    if status:
        rows = c.execute("SELECT * FROM credentials WHERE status=? ORDER BY created_at DESC", (status,)).fetchall()
    else:
        rows = c.execute("SELECT * FROM credentials ORDER BY created_at DESC").fetchall()
    return {"count": len(rows), "credentials": [dict(r) for r in rows]}

class RevokeReq(BaseModel):
    reason: str

@app.post("/api/v1/revoke/{cid}")
def revoke(cid: str, req: RevokeReq):
    c = db()
    row = c.execute("SELECT * FROM credentials WHERE UPPER(id)=UPPER(?)", (cid,)).fetchone()
    if not row:
        raise HTTPException(404, "credential not found")
    c.execute("UPDATE credentials SET status='REVOKED', revoked_reason=? WHERE id=?", (req.reason, row["id"]))
    c.commit()
    return {"revoked": True, "id": row["id"], "reason": req.reason}

# ---- Academy static hosting (pages live in ../design) ----
@app.get("/", response_class=HTMLResponse)
def hub():
    return (DESIGN / "cca-academy-index.html").read_text(errors="replace")

@app.get("/verify", response_class=HTMLResponse)
def verify_ui():
    html = (DESIGN / "cca-academy-verify.html").read_text(errors="replace")
    # point the demo JS at the live API
    html = html.replace("const REG=", "window.LIVE_API='/api/v1'; const DEMO_REG=")
    html += """<script>
(async () => {
  const inp = document.getElementById('qid');
  const orig = window.verify;
  window.verify = async function() {
    const q = inp.value.trim();
    if (!q) return;
    const out = document.getElementById('result');
    out.innerHTML = '<p class="note">Checking registry…</p>';
    try {
      const r = await fetch(`/api/v1/verify/${encodeURIComponent(q)}`);
      const d = await r.json();
      if (!d.found) {
        out.innerHTML = `<div class="vres" style="border-color:rgba(226,178,94,.4)"><div class="micro">RESULT</div>
          <div class="vbig" style="color:var(--gold-txt)">NOT FOUND</div>
          <p class="note">${d.note}</p></div>`;
        return;
      }
      const ok = d.verdict === 'VALID';
      out.innerHTML = `<div class="vres" style="border-color:${ok ? 'var(--green-border)' : 'rgba(226,178,94,.5)'}">
        <div class="micro">RESULT — ${d.verdict}</div>
        <div class="vbig" style="color:${ok ? 'var(--green)' : 'var(--gold-txt)'}">${d.verdict}</div>
        <div class="deflist" style="margin-top:12px">
          <div class="defrow"><span class="dk">Credential ID</span><span class="dv">${d.id}</span></div>
          <div class="defrow"><span class="dk">Course</span><span class="dv">${d.course_title}</span></div>
          <div class="defrow"><span class="dk">Holder</span><span class="dv">${d.holder}</span></div>
          <div class="defrow"><span class="dk">Issued</span><span class="dv">${d.issued}</span></div>
          <div class="defrow"><span class="dk">Expires</span><span class="dv">${d.expires || 'Lifetime'}</span></div>
          <div class="defrow"><span class="dk">Serial</span><span class="dv">${d.serial}</span></div>
        </div></div>`;
    } catch (e) {
      out.innerHTML = `<p class="note">Registry unreachable: ${e}</p>`;
    }
  };
  const qp = new URLSearchParams(location.search).get('id');
  if (qp) { inp.value = qp; window.verify(); }
})();
</script>"""
    return html

@app.get("/courses/{code}", response_class=HTMLResponse)
def course(code: str):
    p = DESIGN / f"cca-academy-{code.lower()}-course.html"
    if not p.exists():
        raise HTTPException(404, "course page not found")
    return p.read_text(errors="replace")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8890)))

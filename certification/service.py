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
    from fastapi import FastAPI, HTTPException, Request, Depends
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

SERVICE_VERSION = os.environ.get("CCA_VERSION", "2.0.3")
app = FastAPI(title="ChainSentry Academy Certification", version=SERVICE_VERSION)

def db():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    c = sqlite3.connect(DB_PATH)
    c.row_factory = sqlite3.Row
    c.execute("""CREATE TABLE IF NOT EXISTS credentials (
        id TEXT PRIMARY KEY, course_code TEXT NOT NULL, course TEXT NOT NULL,
        holder TEXT NOT NULL, email TEXT,
        issued TEXT NOT NULL, expires TEXT, status TEXT NOT NULL DEFAULT 'VALID',
        serial TEXT NOT NULL, revoked_reason TEXT,
        created_at TEXT NOT NULL,
        supersedes TEXT, superseded_by TEXT,
        holder_contact TEXT)""")
    c.execute("ALTER TABLE credentials ADD COLUMN supersedes TEXT") if False else None
    c.execute("""CREATE TABLE IF NOT EXISTS exams (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        credential_id TEXT, course_code TEXT NOT NULL, candidate TEXT NOT NULL,
        started_at TEXT NOT NULL, submitted_at TEXT, score INTEGER,
        pass_mark INTEGER NOT NULL DEFAULT 70, status TEXT NOT NULL DEFAULT 'in_progress',
        attempt INTEGER NOT NULL DEFAULT 1, retake_opens TEXT)""")
    # D2: every verify lookup is logged
    c.execute("""CREATE TABLE IF NOT EXISTS verify_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        queried TEXT NOT NULL, found INTEGER NOT NULL,
        verdict TEXT, ip TEXT, at TEXT NOT NULL)""")
    # D4: voucher/B2B layer
    c.execute("""CREATE TABLE IF NOT EXISTS vouchers (
        code TEXT PRIMARY KEY, course_code TEXT NOT NULL,
        company TEXT NOT NULL, purchased_at TEXT NOT NULL,
        expires_at TEXT NOT NULL, status TEXT NOT NULL DEFAULT 'OPEN',
        redeemed_by TEXT, redeemed_at TEXT, credential_id TEXT,
        order_ref TEXT)""")
    # D6: report-a-fake loop
    c.execute("""CREATE TABLE IF NOT EXISTS fake_reports (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        claimed_code TEXT NOT NULL, reporter_contact TEXT,
        what_was_shown TEXT NOT NULL, reported_at TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'NEW', reviewer_note TEXT)""")
    return c

def _legacy_cols(c):
    """Migration: add phase-2 columns to a pre-existing credentials table (idempotent)."""
    have = {r[1] for r in c.execute("PRAGMA table_info(credentials)").fetchall()}
    for col in ("supersedes", "superseded_by", "holder_contact"):
        if col not in have:
            c.execute(f"ALTER TABLE credentials ADD COLUMN {col} TEXT")
    have2 = {r[1] for r in c.execute("PRAGMA table_info(exams)").fetchall()}
    for col, ddl in (("attempt", "INTEGER NOT NULL DEFAULT 1"), ("retake_opens", "TEXT")):
        if col not in have2:
            c.execute(f"ALTER TABLE exams ADD COLUMN {col} {ddl}")

# ---- Admin token auth (mutations only; reads stay public) ----
from fastapi import Header

ADMIN_TOKEN = os.environ.get("CCA_ADMIN_TOKEN", "")

def require_admin(authorization: str | None = Header(default=None)):
    if not ADMIN_TOKEN:
        return  # auth not configured -> open mode (dev)
    if authorization != f"Bearer {ADMIN_TOKEN}":
        raise HTTPException(401, "admin token required: Authorization: Bearer <token>")

# ---- D1: anti-confusion ID alphabet (no I/L/O/U) — Base58-style ----
SAFE_ALPHABET = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

def safe_token(n: int = 4) -> str:
    return "".join(secrets.choice(SAFE_ALPHABET) for _ in range(n))

def serial_for(code: str) -> str:
    return f"{datetime.datetime.now(datetime.timezone.utc).strftime('%y%m')}-{safe_token(4)}"

def next_number(c, code: str) -> int:
    row = c.execute("SELECT COUNT(*) AS n FROM credentials WHERE course_code=?", (code,)).fetchone()
    return row["n"] + 1

def cred_suffix(num: int) -> str:
    # encoded in the anti-confusion alphabet, not raw decimal
    alpha = SAFE_ALPHABET
    n = num
    out = []
    while n > 0:
        n, r = divmod(n - 1, len(alpha)); out.append(alpha[r])
    s = "".join(reversed(out)) or alpha[0]
    return s.rjust(3, "1")

def cred_id(code: str, num: int) -> str:
    return f"CCA-{code}-{str(datetime.datetime.now(datetime.timezone.utc).year)[-2:]}-{cred_suffix(num)}-{safe_token(4)}"

class IssueReq(BaseModel):
    course_code: str = Field(..., description="BTE|DLF|CAP|CCC|CTX|MTX")
    holder: str
    email: str | None = None

@app.get("/health")
def health():
    c = db(); _legacy_cols(c)
    n = c.execute("SELECT COUNT(*) AS n FROM credentials").fetchone()["n"]
    vl = c.execute("SELECT COUNT(*) AS n FROM verify_log").fetchone()["n"]
    return {"status": "ok", "service": "cca-certification", "version": SERVICE_VERSION,
            "registry_size": n, "verify_lookups_logged": vl, "db": str(DB_PATH),
            "features": ["supersede","voucher","open-badge","fake-report","two-attempt","lookup-log","safe-alphabet"],
            "time": datetime.datetime.now(datetime.timezone.utc).isoformat()}

@app.post("/api/v1/issue", dependencies=[Depends(require_admin)])
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
    c.execute("INSERT INTO credentials VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
              (cid, code, COURSES[code], req.holder, req.email,
               now.date().isoformat(), expires, "VALID", serial,
               None, now.isoformat(timespec="seconds"),
               None, None, req.email))
    c.commit()
    row = c.execute("SELECT * FROM credentials WHERE id=?", (cid,)).fetchone()
    return {"issued": True, "credential": dict(row), "verification_signature": sig,
            "verify_url": f"/api/v1/verify/{cid}"}

@app.get("/api/v1/verify/{cid}")
def verify(cid: str, request: Request = None):
    c = db(); _legacy_cols(c)
    # ID-format lint (helpful NOT_FOUND notes, IDFE-grade)
    bad = [ch for ch in cid if ch in "ILOU"]
    row = c.execute("SELECT * FROM credentials WHERE UPPER(id)=UPPER(?)", (cid,)).fetchone()
    now_iso = datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds")
    ip = request.client.host if request is not None else None
    if not row:
        note = "No credential with this ID in the registry. Check the ID and try again."
        if bad:
            note += " Codes never use the letters I, L, O or U."
        c.execute("INSERT INTO verify_log (queried,found,verdict,ip,at) VALUES (?,?,?,?,?)",
                  (cid, 0, "NOT_FOUND", ip, now_iso)); c.commit()
        return {"found": False, "id": cid, "verdict": "NOT_FOUND", "note": note}
    d = dict(row)
    if d["expires"] and d["expires"] < datetime.date.today().isoformat() and d["status"] == "VALID":
        c.execute("UPDATE credentials SET status='EXPIRED' WHERE id=?", (d["id"],)); c.commit()
        d["status"] = "EXPIRED"
    verdict = d["status"]
    if d.get("superseded_by"):
        verdict = "SUPERSEDED"
    c.execute("INSERT INTO verify_log (queried,found,verdict,ip,at) VALUES (?,?,?,?,?)",
              (cid, 1, verdict, ip, now_iso)); c.commit()
    out = {"found": True, **d, "verdict": verdict,
           "course_title": COURSES.get(d["course_code"], d["course"])}
    if d.get("superseded_by"):
        nxt = c.execute("SELECT id,status FROM credentials WHERE id=?", (d["superseded_by"],)).fetchone()
        out["replaced_by"] = dict(nxt) if nxt else d["superseded_by"]
    return out

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

@app.post("/api/v1/revoke/{cid}", dependencies=[Depends(require_admin)])
def revoke(cid: str, req: RevokeReq):
    c = db()
    row = c.execute("SELECT * FROM credentials WHERE UPPER(id)=UPPER(?)", (cid,)).fetchone()
    if not row:
        raise HTTPException(404, "credential not found")
    c.execute("UPDATE credentials SET status='REVOKED', revoked_reason=? WHERE id=?", (req.reason, row["id"]))
    c.commit()
    return {"revoked": True, "id": row["id"], "reason": req.reason}


# ---- D3: reissue (supersede chain) ----
class ReissueReq(BaseModel):
    new_holder: str
    reason: str = "name change"

@app.post("/api/v1/reissue/{cid}", dependencies=[Depends(require_admin)])
def reissue(cid: str, req: ReissueReq):
    c = db(); _legacy_cols(c)
    row = c.execute("SELECT * FROM credentials WHERE UPPER(id)=UPPER(?)", (cid,)).fetchone()
    if not row:
        raise HTTPException(404, "credential not found")
    old = dict(row)
    if old["status"] != "VALID":
        raise HTTPException(409, f"cannot reissue a {old['status']} credential")
    if old.get("superseded_by"):
        raise HTTPException(409, f"already superseded by {old['superseded_by']}")
    now = datetime.datetime.now(datetime.timezone.utc)
    code = old["course_code"]
    num = next_number(c, code)
    nid = cred_id(code, num)
    vd = VALIDITY_DAYS[code]
    expires = (now + datetime.timedelta(days=vd)).date().isoformat() if vd else None
    serial = serial_for(code)
    c.execute("INSERT INTO credentials VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
              (nid, code, COURSES[code], req.new_holder, old["email"],
               now.date().isoformat(), expires, "VALID", serial,
               None, now.isoformat(timespec="seconds"),
               old["id"], None, old["email"]))
    c.execute("UPDATE credentials SET status='SUPERSEDED', superseded_by=? WHERE id=?", (nid, old["id"]))
    c.commit()
    return {"reissued": True, "old_id": old["id"], "new_id": nid, "new_holder": req.new_holder,
            "reason": req.reason, "verify_old": f"/api/v1/verify/{old['id']}", "verify_new": f"/api/v1/verify/{nid}"}


# ---- D4: voucher/B2B layer ----
class VoucherOrder(BaseModel):
    course_code: str
    company: str
    quantity: int = Field(..., ge=1, le=500)
    order_ref: str | None = None

@app.post("/api/v1/vouchers/order", dependencies=[Depends(require_admin)])
def voucher_order(req: VoucherOrder):
    code = req.course_code.upper()
    if code not in COURSES:
        raise HTTPException(400, f"unknown course {code}")
    c = db()
    now = datetime.datetime.now(datetime.timezone.utc)
    made=[]
    for _ in range(req.quantity):
        vc = f"CCA-V-{safe_token(8)}"
        exp = (now + datetime.timedelta(days=365)).date().isoformat()
        c.execute("INSERT INTO vouchers VALUES (?,?,?,?,?,?,?,?,?,?)",
                  (vc, code, req.company, now.date().isoformat(), exp, "OPEN",
                   None, None, None, req.order_ref))
        made.append(vc)
    c.commit()
    return {"ordered": True, "company": req.company, "course": code,
            "quantity": req.quantity, "vouchers": made,
            "expires": exp, "note": "reassignable until redeemed; results privacy: company sees pass/not only"}

class VoucherRedeem(BaseModel):
    holder: str
    email: str | None = None

@app.post("/api/v1/vouchers/{code}/redeem", dependencies=[Depends(require_admin)])
def voucher_redeem(code: str, req: VoucherRedeem):
    c = db(); _legacy_cols(c)
    row = c.execute("SELECT * FROM vouchers WHERE code=?", (code,)).fetchone()
    if not row:
        raise HTTPException(404, "voucher not found")
    v = dict(row)
    if v["status"] != "OPEN":
        raise HTTPException(409, f"voucher is {v['status']}")
    if v["expires_at"] < datetime.date.today().isoformat():
        c.execute("UPDATE vouchers SET status='EXPIRED' WHERE code=?", (code,)); c.commit()
        raise HTTPException(410, "voucher expired")
    # issue credential tied to redemption
    issue_req = IssueReq(course_code=v["course_code"], holder=req.holder, email=req.email)
    result = issue(issue_req)
    cid = result["credential"]["id"]
    c.execute("UPDATE vouchers SET status='REDEEMED', redeemed_by=?, redeemed_at=?, credential_id=? WHERE code=?",
              (req.holder, datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"), cid, code))
    c.commit()
    return {"redeemed": True, "voucher": code, "credential_id": cid,
            "course": v["course_code"], "company_will_see": ["voucher used", "pass/not"]}

@app.get("/api/v1/vouchers/{code}")
def voucher_status(code: str):
    c = db()
    row = c.execute("SELECT * FROM vouchers WHERE code=?", (code,)).fetchone()
    if not row: raise HTTPException(404, "voucher not found")
    d = dict(row)
    if d.get("credential_id"):
        d["verify_url"] = f"/api/v1/verify/{d['credential_id']}"
    return d

@app.get("/api/v1/vouchers")
def vouchers_by_company(company: str):
    c = db()
    rows = c.execute("SELECT * FROM vouchers WHERE company=? ORDER BY purchased_at DESC", (company,)).fetchall()
    # B2B results privacy: usage + pass/not, never scores
    out=[]
    for r in rows:
        d=dict(r)
        if d.get("credential_id"):
            cred=c.execute("SELECT status FROM credentials WHERE id=?",(d["credential_id"],)).fetchone()
            d["outcome"]= ("passed" if cred and cred["status"] in ("VALID","EXPIRED") else cred["status"] if cred else None)
        out.append({k: d.get(k) for k in ("code","course_code","status","redeemed_by","outcome","expires_at")})
    return {"company": company, "count": len(out), "vouchers": out,
            "privacy": "companies see usage + outcome only; scores and answers stay private"}



# ---- D5: Open Badge v2.0 compatible export ----
BUSINESS_HTML = (APP_DIR / "design" / "business.html").read_text(errors="replace")

BASE_URL = os.environ.get("CCA_BASE_URL", "http://localhost:8890")

@app.get("/api/v1/badge/{cid}")
def open_badge(cid: str):
    c = db(); _legacy_cols(c)
    row = c.execute("SELECT * FROM credentials WHERE UPPER(id)=UPPER(?)", (cid,)).fetchone()
    if not row:
        raise HTTPException(404, "credential not found")
    d = dict(row)
    badge_uid = f"{BASE_URL}/api/v1/verify/{d['id']}"
    ob = {
      "@context": "https://w3id.org/openbadges/v2",
      "type": "Assertion",
      "id": badge_uid,
      "uid": d["serial"],
      "recipient": {"type": "email", "hashed": False, "identity": d["email"] or f"{d['holder']}@unknown.invalid"},
      "issuedOn": d["issued"],
      ("" if not d["expires"] else "expires"): d["expires"],
      "verification": {"type": "hosted", "id": badge_uid},
      "badge": {
        "type": "BadgeClass",
        "id": f"{BASE_URL}/badges/{d['course_code']}",
        "name": d["course"],
        "description": f"ChainSentry Academy certification: {d['course']} (CCA-{d['course_code']}). Vendor-neutral, exam-verified.",
        "image": f"{BASE_URL}/assets/seal-real.png",
        "criteria": {"narrative": "Pass the CCA-{cc} exam at 70% or higher.".format(cc=d["course_code"])},
        "issuer": {
          "type": "Issuer", "id": f"{BASE_URL}/issuer",
          "name": "ChainSentry Academy",
          "url": BASE_URL,
          "description": "Vendor-neutral education for professionals who trace digital evidence."
        }
      }
    }
    if d["status"]=="SUPERSEDED":
        ob["revoked"]=False
    return ob


# ---- D6: report-a-fake loop ----
class FakeReportReq(BaseModel):
    claimed_code: str
    what_was_shown: str
    reporter_contact: str | None = None

@app.post("/api/v1/report-fake")
def report_fake(req: FakeReportReq):
    c = db()
    now = datetime.datetime.now(datetime.timezone.utc)
    rid=f"FR-{now.strftime('%y%m%d')}-{safe_token(4)}"
    c.execute("INSERT INTO fake_reports (claimed_code,reporter_contact,what_was_shown,reported_at,status) VALUES (?,?,?,?,?)",
              (req.claimed_code, req.reporter_contact, req.what_was_shown, now.isoformat(timespec="seconds"), "NEW"))
    c.commit()
    exists = c.execute("SELECT id,status FROM credentials WHERE UPPER(id)=UPPER(?)", (req.claimed_code,)).fetchone()
    return {"report_id": rid, "status": "queued for review",
            "claimed_code_exists_in_registry": bool(exists),
            "registry_verdict_if_genuine": dict(exists) if exists else None,
            "note": "confidential; goes to the review queue"}

@app.get("/api/v1/reports")
def reports(status: str = None):
    c = db()
    if status:
        rows = c.execute("SELECT * FROM fake_reports WHERE status=? ORDER BY reported_at DESC", (status,)).fetchall()
    else:
        rows = c.execute("SELECT * FROM fake_reports ORDER BY reported_at DESC").fetchall()
    return {"count": len(rows), "reports": [dict(r) for r in rows]}

class ReviewReq(BaseModel):
    reviewer_note: str
    mark: str = "REVIEWED"  # REVIEWED|ACTIONED|DISMISSED

@app.post("/api/v1/reports/{rid}/review", dependencies=[Depends(require_admin)])
def review_report(rid: int, req: ReviewReq):
    c = db()
    row = c.execute("SELECT * FROM fake_reports WHERE id=?", (rid,)).fetchone()
    if not row: raise HTTPException(404, "report not found")
    c.execute("UPDATE fake_reports SET status=?, reviewer_note=? WHERE id=?", (req.mark, req.reviewer_note, rid))
    c.commit()
    return {"reviewed": True, "report": rid, "status": req.mark}

# ---- D7: two-attempt exam rule (fail -> retake opens after 7d, free) ----
RETAKE_WAIT_DAYS = 7

class ExamSubmit(BaseModel):
    score: int

@app.post("/api/v1/exam/start", dependencies=[Depends(require_admin)])
def exam_start(course_code: str, candidate: str):
    code = course_code.upper()
    if code not in COURSES:
        raise HTTPException(400, f"unknown course {code}")
    c = db(); _legacy_cols(c)
    now = datetime.datetime.now(datetime.timezone.utc)
    c.execute("INSERT INTO exams (course_code,candidate,started_at,attempt,status) VALUES (?,?,?,?,?)",
              (code, candidate, now.isoformat(timespec="seconds"), 1, "in_progress"))
    c.commit()
    eid = c.execute("SELECT last_insert_rowid() AS id").fetchone()["id"]
    return {"exam_id": eid, "course": code, "candidate": candidate, "attempt": 1,
            "rule": "two attempts in 12 months; pass mark 70; retake (if needed) opens 7 days later at no cost"}

@app.post("/api/v1/exam/{eid}/submit")
def exam_submit(eid: int, req: ExamSubmit):
    c = db(); _legacy_cols(c)
    row = c.execute("SELECT * FROM exams WHERE id=?", (eid,)).fetchone()
    if not row: raise HTTPException(404, "exam not found")
    e = dict(row)
    if e["status"] != "in_progress":
        raise HTTPException(409, f"exam already {e['status']}")
    now = datetime.datetime.now(datetime.timezone.utc)
    passed = req.score >= e["pass_mark"]
    if passed:
        c.execute("UPDATE exams SET score=?, submitted_at=?, status='passed' WHERE id=?",
                  (req.score, now.isoformat(timespec="seconds"), eid))
        c.commit()
        # issue credential on pass
        result = issue(IssueReq(course_code=e["course_code"], holder=e["candidate"]))
        return {"exam_id": eid, "score": req.score, "status": "passed",
                "credential": result["credential"], "attempt": e["attempt"]}
    else:
        attempt = e["attempt"]
        if attempt >= 2:
            c.execute("UPDATE exams SET score=?, submitted_at=?, status='failed_final' WHERE id=?",
                      (req.score, now.isoformat(timespec="seconds"), eid))
            c.commit()
            return {"exam_id": eid, "score": req.score, "status": "failed_final",
                    "note": "both attempts used; purchase a new voucher to retake"}
        retake_opens = (now + datetime.timedelta(days=RETAKE_WAIT_DAYS)).date().isoformat()
        c.execute("UPDATE exams SET score=?, submitted_at=?, status='failed_retry_scheduled', attempt=2, retake_opens=? WHERE id=?",
                  (req.score, now.isoformat(timespec="seconds"), retake_opens, eid))
        c.commit()
        return {"exam_id": eid, "score": req.score, "status": "failed_retry_scheduled",
                "attempt_used": attempt, "retake_opens": retake_opens,
                "note": "second attempt opens in 7 days at no cost"}

@app.post("/api/v1/exam/{eid}/retake")
def exam_retake(eid: int):
    c = db(); _legacy_cols(c)
    row = c.execute("SELECT * FROM exams WHERE id=?", (eid,)).fetchone()
    if not row: raise HTTPException(404, "exam not found")
    e = dict(row)
    if e["status"] != "failed_retry_scheduled":
        raise HTTPException(409, f"retake not scheduled (status: {e['status']})")
    today = datetime.date.today().isoformat()
    if (e.get("retake_opens") or "9999-12-31") > today:
        raise HTTPException(425, f"retake opens {e['retake_opens']}; too early")
    now = datetime.datetime.now(datetime.timezone.utc)
    c.execute("UPDATE exams SET started_at=?, status='in_progress' WHERE id=?",
              (now.isoformat(timespec="seconds"), eid))
    c.commit()
    return {"exam_id": eid, "attempt": 2, "status": "in_progress",
            "rule": "final attempt; pass mark 70"}

@app.get("/api/v1/verify-log")
def verify_log_tail(limit: int = 25):
    c = db()
    rows = c.execute("SELECT * FROM verify_log ORDER BY id DESC LIMIT ?", (limit,)).fetchall()
    return {"count": len(rows), "entries": [dict(r) for r in rows]}
# ---- Certificate PDF renderer (reportlab + qrcode, generated on demand) ----
import io as _io

def _cert_pdf(d: dict) -> bytes:
    """Legacy inline renderer (fallback; the canonical layout lives in certdesign.py)."""
    from reportlab.lib.pagesizes import A4, landscape
    from reportlab.lib.units import mm
    from reportlab.lib.colors import HexColor
    from reportlab.pdfgen import canvas as _canvas
    import qrcode as _qrcode

    NAVY = HexColor("#12263F"); GOLD = HexColor("#B8860B"); GREY = HexColor("#5A6672")
    buf = _io.BytesIO()
    W, H = landscape(A4)
    cv = _canvas.Canvas(buf, pagesize=(W, H))
    cv.setStrokeColor(NAVY); cv.setLineWidth(2)
    cv.rect(14*mm, 14*mm, W-28*mm, H-28*mm)
    cv.setStrokeColor(GOLD); cv.setLineWidth(0.8)
    cv.rect(17*mm, 17*mm, W-34*mm, H-34*mm)
    seal_path = APP_DIR / "assets" / "seal-real.png"
    from reportlab.lib.utils import ImageReader as _IR
    if seal_path.exists():
        cv.drawImage(_IR(str(seal_path)), 30*mm, H/2-23*mm, 46*mm, 46*mm, mask="auto")
    cv.setFillColor(NAVY); cv.setFont("Helvetica-Bold", 11)
    cv.drawCentredString(W/2, H-32*mm, "CHAINSENTRY ACADEMY")
    cv.setFont("Helvetica-Bold", 26)
    cv.drawCentredString(W/2, H-45*mm, "CERTIFICATE OF COMPLETION")
    cv.setFont("Helvetica", 12); cv.setFillColor(GREY)
    cv.drawCentredString(W/2, H-58*mm, "This certifies that")
    cv.setFillColor(NAVY); cv.setFont("Helvetica-Bold", 22)
    cv.drawCentredString(W/2, H-68*mm, d["holder"][:44])
    cv.setFont("Helvetica", 12); cv.setFillColor(GREY)
    cv.drawCentredString(W/2, H-78*mm, "has passed the examination for")
    cv.setFillColor(NAVY); cv.setFont("Helvetica-Bold", 17)
    cv.drawCentredString(W/2, H-88*mm, d["course"])
    cv.setFont("Helvetica", 10); cv.setFillColor(GREY)
    cv.drawString(60*mm, 30*mm, f"Credential ID: {d['id']}")
    cv.drawString(60*mm, 24*mm, f"Issued: {d['issued']}    Serial: {d['serial']}")
    cv.drawRightString(W-60*mm, 24*mm, f"Valid: {d['expires'] or 'Lifetime'}    Status: {d['status']}")
    import urllib.parse
    base = os.environ.get("CCA_BASE_URL", "http://localhost:8890")
    vurl = f"{base}/verify?id={urllib.parse.quote(d['id'])}"
    qr = _qrcode.QRCode(box_size=4, border=1)
    qr.add_data(vurl); qr.make(fit=True)
    qimg = qr.make_image(fill_color="#12263F", back_color="white")
    qbuf = _io.BytesIO(); qimg.save(qbuf, format="PNG"); qbuf.seek(0)
    cv.drawImage(_IR(qbuf), W-52*mm, 20*mm, 24*mm, 24*mm)
    cv.setFont("Helvetica", 7)
    cv.drawCentredString(W-40*mm, 18.5*mm, "Scan to verify")
    cv.showPage(); cv.save()
    return buf.getvalue()

@app.get("/certificate/{cid}.pdf")
def certificate_pdf(cid: str):
    c = db(); _legacy_cols(c)
    row = c.execute("SELECT * FROM credentials WHERE UPPER(id)=UPPER(?)", (cid,)).fetchone()
    if not row:
        raise HTTPException(404, "credential not found")
    from fastapi.responses import Response
    d = dict(row)
    try:
        import sys as _sys
        if str(APP_DIR) not in _sys.path: _sys.path.insert(0, str(APP_DIR))
        from certdesign import cert_pdf as _layout
        pdf = _layout(holder=d["holder"], course=d["course"], cid=d["id"],
                      issued=d["issued"], serial=d["serial"], expires=d["expires"],
                      status=d["status"], base_url=os.environ.get("CCA_BASE_URL", "http://localhost:8890"),
                      seal_path=str(APP_DIR / "assets" / "seal-real.png"))
    except Exception:
        pdf = _cert_pdf(d)  # legacy fallback
    return Response(pdf, media_type="application/pdf",
                    headers={"Content-Disposition": f'inline; filename="CCA-{row["id"]}.pdf"'})

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

@app.get("/business", response_class=HTMLResponse)
def business_page():
    return BUSINESS_HTML

@app.get("/assets/{fname}")
def assets(fname: str):
    p = APP_DIR / "assets" / fname
    if not p.exists():
        raise HTTPException(404, "asset not found")
    mime = "image/png" if fname.endswith(".png") else "image/svg+xml" if fname.endswith(".svg") else "application/octet-stream"
    from fastapi.responses import Response
    return Response(p.read_bytes(), media_type=mime)

@app.get("/courses/{code}", response_class=HTMLResponse)
def course(code: str):
    p = DESIGN / f"cca-academy-{code.lower()}-course.html"
    if not p.exists():
        raise HTTPException(404, "course page not found")
    return p.read_text(errors="replace")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8890)))

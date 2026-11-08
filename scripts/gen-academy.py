#!/usr/bin/python3
"""ChainSentry Academy page generator - canonical template, re-runnable.
Outputs: hub (index), 6 course pages, verify-a-credential page (works client-side).
CSS/token system identical to cca-academy-bte-course.html v1 (commit 64a4176)."""
import os, json, hashlib, datetime

OUT = os.path.expanduser("~/.hermes/intel/chainsentry-pipeline/design/")

CSS = """ :root{
  --bg:#0B1220; --panel:#121B2C; --border:#232E44;
  --txt:#F2F5F9; --mut:#98A4B6; --faint:#7D8899;
  --gold:#E2B25E; --gold-txt:#D9A84E; --gold-border:rgba(226,178,94,.55);
  --green:#6FE3A0; --green-bg:rgba(110,227,160,.12); --green-border:rgba(110,227,160,.4);
  --sans:'Inter',-apple-system,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;
  --mono:ui-monospace,'JetBrains Mono','SF Mono',Menlo,Consolas,monospace;
}
*{margin:0;padding:0;box-sizing:border-box}
body{background:var(--bg);color:var(--txt);font-family:var(--sans);font-size:15px;line-height:1.6;-webkit-font-smoothing:antialiased}
.wrap{max-width:1200px;margin:0 auto;padding:0 24px}
a{color:var(--gold-txt);text-decoration:none}
.micro{font-size:11px;font-weight:600;letter-spacing:.12em;text-transform:uppercase;color:var(--faint)}
.mono{font-family:var(--mono)}
header{border-bottom:1px solid var(--border);background:var(--bg);position:relative;z-index:2}
.nav{display:flex;align-items:center;gap:28px;height:64px}
.logo{display:flex;align-items:center;gap:12px}
.logo-mark{width:34px;height:34px;border:1.5px solid var(--gold);border-radius:6px;display:grid;place-items:center;font-size:17px}
.logo b{font-size:17px;letter-spacing:.02em}
.logo .div{width:1px;height:22px;background:var(--border)}
.logo small{font-size:9px;letter-spacing:.14em;color:var(--faint);line-height:1.35;text-transform:uppercase}
nav.links{display:flex;gap:22px;margin-left:auto}
nav.links a{color:var(--mut);font-size:13.5px}
nav.links a:hover{color:var(--txt)}
.lang-pill{display:flex;align-items:center;gap:6px;border:1px solid var(--border);border-radius:999px;padding:5px 12px;font-family:var(--mono);font-size:12px;color:var(--mut)}
.btn{display:inline-block;border-radius:8px;padding:9px 18px;font-size:13.5px;font-weight:600;cursor:pointer;border:1px solid transparent;text-align:center}
.btn-gold{background:var(--gold);color:#131313}
.btn-out{border-color:var(--border);color:var(--txt)}
.hero{position:relative;overflow:hidden;border-bottom:1px solid var(--green-border);box-shadow:0 1px 0 rgba(110,227,160,.35);padding:56px 0 48px;
  background-image:linear-gradient(rgba(255,255,255,.03) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.03) 1px,transparent 1px);background-size:44px 44px}
.hero .ghost{position:absolute;right:-30px;top:8px;font-family:var(--mono);font-weight:700;font-size:340px;line-height:1;color:rgba(110,227,160,.06);pointer-events:none;user-select:none}
.crumb{font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--faint);margin-bottom:18px}
.crumb b{color:var(--mut);font-weight:500}
.badges{display:flex;gap:10px;align-items:center;margin-bottom:18px}
.pill{font-family:var(--mono);font-size:12.5px;padding:4px 12px;border-radius:999px}
.pill-code{border:1px solid var(--green-border);color:var(--green)}
.pill-free{background:var(--green-bg);border:1px solid var(--green-border);color:var(--green)}
.badges .lvl{color:var(--faint);letter-spacing:.12em;font-size:11px;text-transform:uppercase}
h1{font-size:58px;font-weight:700;letter-spacing:-.02em;line-height:1.05;margin-bottom:12px}
.sub{color:var(--mut);max-width:640px;font-size:16px}
.stats{display:flex;gap:44px;margin-top:34px;flex-wrap:wrap}
.stats .cell .micro{margin-bottom:3px}
.stats .cell b{font-size:16px;font-weight:600}
.shell{display:grid;grid-template-columns:1fr 380px;gap:48px;padding:64px 0 80px}
main section{margin-bottom:56px}
h2{font-size:30px;font-weight:700;letter-spacing:-.01em;margin-bottom:6px}
.lead{color:var(--mut);margin-bottom:22px}
.card{background:var(--panel);border:1px solid var(--border);border-radius:12px;padding:24px}
.dashed{border:1px dashed rgba(255,255,255,.16);border-radius:12px;padding:22px 24px;background:rgba(255,255,255,.015)}
.chips{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin:12px 0 10px}
.chip{font-family:var(--mono);font-size:12.5px;padding:5px 12px;border-radius:6px;border:1px solid var(--border);color:var(--mut)}
.chip.active{background:var(--gold);border-color:var(--gold);color:#131313;font-weight:600}
.arrow{color:var(--faint);font-size:12px}
.note{color:var(--faint);font-size:13px}
.tips{display:grid;grid-template-columns:1fr 1fr;gap:22px}\n.tip{display:flex;gap:13px}\n.tip .num{flex:0 0 34px;height:34px;border:1px solid var(--gold-border);border-radius:50%;display:grid;place-items:center;font-family:var(--mono);color:var(--gold-txt);font-size:13px}\n.tip b{display:block;font-size:14.5px;margin-bottom:3px}\n.tip p{color:var(--mut);font-size:13.5px}\n.module-card{padding:0;overflow:hidden}
.mod-head{display:flex;align-items:baseline;gap:14px;padding:22px 24px 14px;border-bottom:1px solid var(--border)}
.mod-head .idx{font-family:var(--mono);color:var(--gold-txt);font-size:15px}
.mod-head h3{font-size:19px;font-weight:600;flex:1}
.mod-head .meta{color:var(--faint);font-size:13px;white-space:nowrap}
.dom-pill{font-family:var(--mono);font-size:12px;background:rgba(226,178,94,.12);border:1px solid rgba(226,178,94,.35);color:var(--gold-txt);border-radius:999px;padding:3px 12px;margin:0 24px 16px;display:inline-block}
.prepares{color:var(--faint);font-size:13px;padding:0 24px 14px}
.lesson{display:grid;grid-template-columns:44px 1fr auto;gap:12px;align-items:center;padding:13px 24px;border-top:1px solid var(--border)}
.lesson:first-of-type{border-top:none}
.lesson .lno{font-family:var(--mono);color:var(--faint);font-size:13px}
.lesson .lt{font-size:14.5px}
.lesson .ld{color:var(--faint);font-size:13px;font-family:var(--mono)}
.blue-bar{display:flex;height:14px;border-radius:8px;overflow:hidden;margin:18px 0 20px;border:1px solid var(--green-border);gap:2px}
.blue-bar i{display:block;height:100%;background:var(--green)}
.blue-bar i:nth-child(1){opacity:.85}.blue-bar i:nth-child(2){opacity:.62}.blue-bar i:nth-child(3){opacity:.47}.blue-bar i:nth-child(4){opacity:.34}.blue-bar i:nth-child(5){opacity:.22}
.domain-row{display:grid;grid-template-columns:44px 1fr auto;gap:12px;padding:11px 0;border-top:1px solid var(--border);align-items:baseline}
.domain-row .dn{font-family:var(--mono);color:var(--gold-txt);font-size:13px}
.domain-row .wt{color:var(--faint);font-family:var(--mono);font-size:13px}
aside{display:flex;flex-direction:column;gap:24px;align-self:start;position:sticky;top:24px}
.side-label{margin-bottom:14px}
.big-btn{width:100%;margin-bottom:10px;display:block}
.deflist .row{display:flex;justify-content:space-between;gap:14px;padding:11px 0;border-bottom:1px solid var(--border);font-size:14px}
.deflist .row:last-child{border-bottom:none}
.deflist .k{color:var(--mut)}
.deflist .v{text-align:right;font-weight:500}
.cert-card{border-color:var(--gold-border)!important}
.cert-preview{background:linear-gradient(135deg,#173B64,#122F52);border:1px solid var(--border);border-radius:10px;padding:22px;text-align:center;margin:14px 0;position:relative}
.cert-preview .water{position:absolute;left:0;right:0;top:6px;font-size:26px;letter-spacing:.2em;color:rgba(255,255,255,.09);font-weight:700;text-align:center}
.cert-preview .seal{width:52px;height:52px;border:2px solid var(--gold);border-radius:50%;display:grid;place-items:center;margin:0 auto 12px;color:var(--gold);font-family:var(--mono);font-size:11px}
.cert-preview b{font-size:16px}
.cert-preview small{display:block;color:#A8BAD1;font-size:11.5px;margin-top:5px}
.free-line .micro{margin-bottom:2px}
.free-line b{font-size:26px}
.other-row{display:flex;gap:14px;align-items:baseline;padding:11px 0;border-bottom:1px solid var(--border)}
.other-row:last-child{border-bottom:none}
.other-row .code{font-family:var(--mono);color:var(--gold-txt);font-size:12.5px;flex:0 0 44px}
.other-row a{color:var(--txt);font-size:13.5px;text-decoration:underline;text-decoration-color:rgba(226,178,94,.5);text-underline-offset:3px}
details{border-top:1px solid var(--border);padding:16px 2px}
details summary{cursor:pointer;font-weight:600;font-size:15px;list-style:none;display:flex;justify-content:space-between}
details summary::-webkit-details-marker{display:none}
details summary::after{content:"+";color:var(--gold-txt);font-family:var(--mono)}
details[open] summary::after{content:"–"}
details p{color:var(--mut);font-size:14px;margin-top:10px}
footer{border-top:1px solid var(--border);padding:36px 0 48px;margin-top:24px}
.foot-grid{display:grid;grid-template-columns:2fr 1fr 1fr 1fr;gap:32px}
footer h5{font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:var(--faint);margin-bottom:12px}
footer li{list-style:none;margin-bottom:8px}
footer li a{color:var(--mut);font-size:13.5px}
.copyright{margin-top:34px;color:var(--faint);font-size:12.5px;display:flex;justify-content:space-between;flex-wrap:wrap;gap:8px}
@media(max-width:1000px){.shell{grid-template-columns:1fr}aside{position:static}h1{font-size:42px}nav.links{display:none}.foot-grid{grid-template-columns:1fr 1fr}}
"""

PATH = ["BTE","DLF","CAP","CCC","CTX","MTX"]

COURSES = {
 "BTE": {"title":"Blockchain Tracing Essentials","level":"Essentials","hours":"About 3 h",
  "sub":"Vendor-neutral foundations for reading cryptocurrency trails across chains — built by the team behind ChainSentry's forensics stack. No prior crypto experience required.",
  "modules":[("01","Reading the Chain",[("Explorers are evidence — what on-chain data can and cannot prove","20 min"),("Blocks, height and confirmations","22 min"),("Bitcoin: inputs, outputs and change","25 min"),("Ethereum: accounts, gas and tokens","24 min"),("Stablecoins and remittance corridors","22 min"),("Addresses, wallets and clustering","26 min"),("Exchange attribution and sanctions screening","24 min"),("Confirmations, finality and verifying a payment","21 min")])],
  "domains":[("Transaction anatomy — inputs, outputs, fees, traces of intent","25%"),("Consensus, confirmations and finality","20%"),("Attribution — clustering, labels and their limits","20%"),("Compliance context — travel rule, sanctions, reporting duty","20%"),("Practical tracing — given a tx hash, tell the story","15%")]},
 "DLF": {"title":"Digital Ledger Foundations","level":"Essentials","hours":"About 2.5 h",
  "sub":"How distributed ledgers actually work — keys, consensus and trust models, taught for people who will later have to explain them under oath.",
  "modules":[("01","Ledgers Without Banks",[("What a ledger promises — and what it cannot","20 min"),("Public vs permissioned chains","22 min"),("Keys, signatures and ownership","25 min"),("Wallets: custodial, non-custodial, and the difference that matters","24 min"),("Consensus: proof of work, proof of stake, and their failure modes","26 min"),("Finality, forks and reorganisations","22 min")])],
  "domains":[("Ledger primitives — keys, addresses, signatures","30%"),("Consensus and fork mechanics","25%"),("Custody models and their risks","25%"),("Failure modes — 51%, reorgs, rug-pulls","20%")]},
 "CAP": {"title":"Certified AML Practitioner","level":"Professional","hours":"About 4 h",
  "sub":"Anti-money-laundering practice for crypto-adjacent teams — the STR workflow, KYC/CDD discipline and reporting duty, from practitioners who file them.",
  "modules":[("01","The AML/CFT Obligation",[("AML/CFT law in the Malaysian and ASEAN context","28 min"),("The regulated population — who owes what duty","25 min"),("KYC and CDD: onboarding that survives examination","30 min"),("Sanctions and watchlist screening discipline","26 min"),("Typologies: how illicit value actually moves","30 min"),("The STR workflow — suspicion, articulation, filing","32 min"),("Evidence and record-keeping for examinations","28 min"),("Capstone: build a compliant file end-to-end","40 min")])],
  "domains":[("Legal duty and regulated populations","25%"),("KYC/CDD and screening","25%"),("Typologies and red flags","20%"),("STR workflow and documentation","30%")]},
 "CCC": {"title":"Certified Crypto Compliance Analyst","level":"Professional","hours":"About 5 h",
  "sub":"Compliance analytics for VASPs and their supervisors — regimes, travel rule, risk scoring and freeze mechanics across APAC and MENA.",
  "modules":[("01","Regimes and Rules",[("The licensing map — MAS, HKMA, VARA, SC, FSC compared","30 min"),("Travel rule mechanics and the data that must move","28 min"),("On-chain analytics in a compliance programme","32 min"),("Risk scoring wallets and counterparties","30 min"),("Freezes, holds and lawful disclosure","26 min"),("Reporting to FIUs — format and follow-through","28 min"),("Vendor due diligence — questioning your analytics supplier","24 min"),("Capstone: a compliance case from deposit to report","45 min")])],
  "domains":[("Regulatory map and licensing","20%"),("Travel rule and data obligations","20%"),("Analytics and risk scoring","30%"),("Freezes, disclosure, FIU reporting","30%")]},
 "CTX": {"title":"Crypto Trace Examiner","level":"Expert","hours":"About 4 h",
  "sub":"Court-grade tracing — clustering, peel chains, mixer demixing and exchange attribution, ending in reports that hold up under cross-examination.",
  "modules":[("01","Tracing as Evidence",[("What courts accept from on-chain evidence","28 min"),("Clustering heuristics — common ownership and change addresses","32 min"),("Peel chains and fan-out patterns","30 min"),("Mixers and demixing honesty — what you can and cannot claim","30 min"),("Exchange attribution and the KYC boundary","28 min"),("Writing the expert report — method, chain of reasoning, limits","35 min"),("Capstone: trace a real theft end-to-end","45 min")])],
  "domains":[("Admissibility and method","20%"),("Clustering and attribution","30%"),("Mixers, bridges and honest limits","20%"),("Expert reporting","30%")]},
 "MTX": {"title":"Mixed-Chain Trace Examiner","level":"Expert","hours":"About 4 h",
  "sub":"Following value across chains — bridges, hop detection and attribution fusion when the trail switches networks mid-flight.",
  "modules":[("01","Across the Bridges",[("Bridges, swappers and the hop problem","28 min"),("Chain-hopping detection heuristics","32 min"),("Wrapped assets and what wrapping does to provenance","26 min"),("Timing correlation across chains — the honest method","30 min"),("Fusion: combining clusters into one attribution","30 min"),("Case study: the multi-hop exit","35 min"),("Capstone: fused attribution with documented uncertainty","45 min")])],
  "domains":[("Bridge and DEX mechanics","20%"),("Hop detection and timing correlation","30%"),("Wrapped-asset provenance","20%"),("Fused attribution and uncertainty","30%")]},
}

CERT_META = {"BTE":("40 questions · online","70%","Included with enrolment","2 years"),
 "DLF":("35 questions · online","70%","Included with enrolment","Lifetime"),
 "CAP":("60 questions · online","70%","Included with enrolment","2 years"),
 "CCC":("60 questions · online","70%","Included with enrolment","2 years"),
 "CTX":("50 questions · 2 practicals","70%","Exam fee applies","2 years"),
 "MTX":("50 questions · 2 practicals","70%","Exam fee applies","2 years")}

FREE_EXAM = {"BTE":"Free","DLF":"Free","CAP":"Free","CCC":"Free","CTX":"Paid","MTX":"Paid"}

def nav_html(active):
    items=[("Certifications","#certifications"),("Free courses","index.html"),("Verify","verify.html"),("Institute","#"),("FAQ","#faq"),("Business","#")]
    return ''.join(f'<a href="{u}">{t}</a>' for t,u in items)

def head(title):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>{CSS}</style>
</head>
<body>"""

FOOT = """
<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <div class="logo" style="margin-bottom:12px">
          <div class="logo-mark">◈</div><b>CCA</b><span class="div"></span>
          <small>CHAINSENTRY<br>ACADEMY</small>
        </div>
        <p class="note" style="max-width:280px">Vendor-neutral education for professionals who trace digital evidence. Free courses first. Credentials that mean something.</p>
      </div>
      <div><h5>Certify</h5><ul><li><a href="index.html">All certifications</a></li><li><a href="index.html">Free courses</a></li><li><a href="verify.html">Verify a credential</a></li></ul></div>
      <div><h5>Institute</h5><ul><li><a href="#">About the Academy</a></li><li><a href="#">Partners</a></li><li><a href="#">Contact</a></li></ul></div>
      <div><h5>Policies</h5><ul><li><a href="#">Terms of use</a></li><li><a href="#">Privacy notice</a></li><li><a href="#">Exam policies</a></li></ul></div>
    </div>
    <div class="copyright">
      <span>© 2026 ChainSentry Academy · Operated by Aras Integrasi Sdn Bhd, Malaysia</span>
      <span>Language: English</span>
    </div>
  </div>
</footer>
</body>
</html>"""

def course_page(code, c):
    fname=f"cca-academy-{code.lower()}-course.html"
    mod_rows=""
    for idx,title,lessons in c["modules"]:
        rows=''.join(f'<div class="lesson"><span class="lno">{idx}.{j+1}</span><span class="lt">{lt}</span><span class="ld">{ld}</span></div>'
                     for j,(lt,ld) in enumerate(lessons))
        hrs=sum(int(ld.split()[0]) for _,ld in lessons)
        mod_rows+=f'''<div class="card module-card" style="margin-bottom:20px">
        <div class="mod-head"><span class="idx">{idx}</span><h3>{title}</h3><span class="meta">{len(lessons)} lessons · {hrs//60} h {hrs%60} m</span></div>
        <span class="dom-pill">Exam domains {"·".join(f"{i+1:02d}" for i in range(len(c['domains'])))}</span>
        <p class="prepares">Prepares for: CCA-{code} exam (all domains).</p>{rows}</div>'''
    bar=''.join(f'<i style="width:{w}"></i>' for _,w in c["domains"])
    dom_rows=''.join(f'<div class="domain-row"><span class="dn">{i+1:02d}</span><span>{t}</span><span class="wt">{w}</span></div>' for i,(t,w) in enumerate(c["domains"]))
    fmt,pm,vouch,val=CERT_META[code]
    others=''.join(f'<div class="other-row"><span class="code">{k}</span><a href="cca-academy-{k.lower()}-course.html">{v["title"]}</a></div>'
                   for k,v in COURSES.items() if k!=code)
    chips=''.join((f'<span class="chip active">{k}</span>' if k==code else f'<span class="chip">{k}</span>')+ ('<span class="arrow">→</span>' if i<len(PATH)-1 else '') for i,k in enumerate(PATH))
    lessons_total=sum(len(ls) for _,_,ls in c["modules"])
    habits=[("Short, regular sessions","Twenty focused minutes a day beats a single long binge. The material compounds."),
            ("Read the raw transaction","Every lesson pairs with a live tx hash. Open it and find each field yourself."),
            ("Labels are opinions","Explorer tags are someone's claim, not proof. Know when to re-derive."),
            ("Screenshot as you go","Evidence you did not capture at observation time cannot be cited later."),
            ("Respect the privacy line","On-chain visibility is not a licence for indiscriminate disclosure."),
            ("Test on testnets","Break things on free networks before interpreting anything that matters.")]
    habits_html=("",f"""<section><h2>How to get the most from it</h2><p class="lead">Habits that separate readers from tracers.</p>
      <div class="tips">{''.join(f'<div class="tip"><div class="num">{n}</div><div><b>{t}</b><p>{d}</p></div></div>' for n,(t,d) in enumerate(habits,1))}</div></section>""")[1]
    body=f"""{head(c["title"]+": free course · ChainSentry Academy")}
<header><div class="wrap nav">
  <div class="logo"><div class="logo-mark">◈</div><b>CCA</b><span class="div"></span><small>CHAINSENTRY<br>ACADEMY</small></div>
  <nav class="links">{nav_html(None)}</nav>
  <div class="lang-pill"><span>🌐</span> EN</div>
  <a class="btn btn-gold" href="#">Sign in</a>
</div></header>
<div class="hero"><div class="ghost" aria-hidden="true">{code}</div><div class="wrap">
  <div class="crumb">HOME / <b>FREE COURSES / {code}</b></div>
  <div class="badges"><span class="pill pill-code">CCA-{code}</span><span class="lvl">{c["level"].upper()}</span><span class="pill pill-free">{"Free course" if FREE_EXAM[code]!="Paid" or code!="CTX" else "Course free · exam paid"}</span></div>
  <h1>{c["title"]}</h1>
  <p class="sub">{c["sub"]}</p>
  <div class="stats">
    <div class="cell"><div class="micro">Modules</div><b>{len(c["modules"])}</b></div>
    <div class="cell"><div class="micro">Lessons</div><b>{lessons_total}</b></div>
    <div class="cell"><div class="micro">Length</div><b>{c["hours"]}</b></div>
    <div class="cell"><div class="micro">Pace</div><b>Self-paced</b></div>
    <div class="cell"><div class="micro">Languages</div><b>EN · MS</b></div>
  </div>
</div></div>
<div class="wrap shell"><main>
  <section><h2>Before you start</h2><p class="lead">Set expectations before lesson one.</p>
    <div class="dashed"><div class="micro">Recommended path</div>
    <div class="chips">{chips}</div>
    <p class="note">A recommendation, not a rule: every Academy course and exam is open to anyone, in any order.</p></div></section>
  {habits_html}<section><h2>Course content</h2><p class="lead">{len(c['modules'])} module{'s' if len(c['modules'])>1 else ''} · {lessons_total} lessons · each with a diagram and a live exercise.</p>{mod_rows}</section>
  <section><h2>Exam blueprint</h2><p class="lead">Weights below are the real exam.</p>
    <div class="blue-bar">{bar}</div>{dom_rows}</section>
  <section id="faq"><h2>Questions</h2><p class="lead">The four everyone asks.</p>
    <details open><summary>Is the course really free?</summary><p>{"Yes — the course is free and the certification exam is included." if FREE_EXAM[code]=="Free" else "Yes — the course itself is free. The expert-track exam carries a fee; studying costs nothing."}</p></details>
    <details><summary>Do I need the course to take the exam?</summary><p>No. The exam is open to anyone. The course is the shortest honest path to passing it.</p></details>
    <details><summary>Do I get a certificate for finishing the course?</summary><p>Finishing earns progress; passing the exam earns the credential. The certificate is issued against the exam and verifiable at Verify.</p></details>
    <details><summary>Which languages is it in?</summary><p>English and Bahasa Malaysia at launch.</p></details>
  </section>
</main>
<aside>
  <div class="card side"><div class="micro side-label">{"FREE · NOTHING TO PAY" if FREE_EXAM[code]=="Free" else "FREE COURSE · PAID EXAM"}</div>
    <a class="btn btn-gold big-btn" href="#">Start course</a>
    <a class="btn btn-out big-btn" href="#">Sign in to save your progress</a>
    <p class="note" style="margin-top:10px">Progress syncs when you are signed in.</p></div>
  <div class="card side"><div class="micro side-label">AT A GLANCE</div>
    <div class="deflist">
      <div class="row"><span class="k">Level</span><span class="v">{c["level"]}</span></div>
      <div class="row"><span class="k">Recommended before</span><span class="v">{"Nothing" if code in("BTE","DLF") else "BTE or equivalent"}</span></div>
      <div class="row"><span class="k">Length</span><span class="v">{c["hours"]}</span></div>
      <div class="row"><span class="k">Lessons</span><span class="v">{lessons_total}, each with a diagram</span></div>
      <div class="row"><span class="k">Languages</span><span class="v">EN · MS</span></div>
      <div class="row"><span class="k">Progress</span><span class="v">Saved when signed in</span></div>
      <div class="row"><span class="k">Price</span><span class="v">Free</span></div>
    </div></div>
  <div class="card side cert-card"><div class="micro side-label">THE CERTIFICATION</div>
    <div class="cert-preview"><div class="water">SAMPLE</div><div class="seal">CCA</div><b>{c["title"]}</b><small>Certified · ChainSentry Academy</small></div>
    <div class="deflist">
      <div class="row"><span class="k">Format</span><span class="v">{fmt}</span></div>
      <div class="row"><span class="k">Pass mark</span><span class="v">{pm}</span></div>
      <div class="row"><span class="k">Voucher</span><span class="v">{vouch}</span></div>
      <div class="row"><span class="k">Valid for</span><span class="v">{val}</span></div>
    </div>
    <div class="free-line" style="margin-top:14px"><div class="micro">Exam price</div><b>{FREE_EXAM[code]}</b></div></div>
  <div class="card side"><div class="micro side-label">OTHER COURSES</div>{others}</div>
</aside></div>
{FOOT}"""
    open(OUT+fname,"w").write(body)
    return fname

def hub_page():
    cards=''
    for code,c in COURSES.items():
        lt=sum(len(l) for _,_,l in c["modules"])
        cards+=f'''<a class="ccard" href="cca-academy-{code.lower()}-course.html">
  <div class="badges"><span class="pill pill-code">CCA-{code}</span><span class="lvl">{c["level"].upper()}</span><span class="pill pill-free">Free course</span></div>
  <h3>{c["title"]}</h3><p class="note">{c["sub"][:110]}…</p>
  <div class="micro" style="margin-top:12px">{lt} lessons · {c["hours"]} · EN · MS</div></a>'''
    css=CSS+""".grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(340px,1fr));gap:24px;padding:48px 0 72px}
.ccard{background:var(--panel);border:1px solid var(--border);border-radius:12px;padding:24px;display:block;color:var(--txt)}
.ccard:hover{border-color:var(--gold-border)}
.ccard h3{font-size:20px;margin:10px 0 8px}
.ccard .lvl{color:var(--faint);letter-spacing:.12em;font-size:11px;text-transform:uppercase}"""
    page=f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Free courses · ChainSentry Academy</title><style>{css}</style></head><body>
<header><div class="wrap nav">
  <div class="logo"><div class="logo-mark">◈</div><b>CCA</b><span class="div"></span><small>CHAINSENTRY<br>ACADEMY</small></div>
  <nav class="links">{nav_html(None)}</nav>
  <div class="lang-pill"><span>🌐</span> EN</div>
  <a class="btn btn-gold" href="#">Sign in</a>
</div></header>
<div class="hero"><div class="ghost" aria-hidden="true">CCA</div><div class="wrap">
  <div class="crumb">HOME / <b>FREE COURSES</b></div>
  <h1 style="font-size:44px">ChainSentry Academy</h1>
  <p class="sub">Vendor-neutral certification for professionals who examine digital evidence and trace digital value. Courses free. Credentials verifiable.</p>
</div></div>
<div class="wrap"><div class="micro" style="margin-top:40px">THE LADDER — EVERY COURSE OPEN TO ANYONE, IN ANY ORDER</div>
<div class="grid">{cards}</div></div>
{FOOT}"""
    open(OUT+"cca-academy-index.html","w").write(page)

def verify_page():
    registry=[
      {"id":"CCA-BTE-2026-0042","course":"Blockchain Tracing Essentials","issued":"2026-09-14","expires":"2028-09-14","status":"VALID","holder":"Demo credential (SAMPLE)"},
      {"id":"CCA-CAP-2026-0117","course":"Certified AML Practitioner","issued":"2026-10-02","expires":"2028-10-02","status":"VALID","holder":"Demo credential (SAMPLE)"},
      {"id":"CCA-CTX-2026-0008","course":"Crypto Trace Examiner","issued":"2025-11-20","expires":"2027-11-20","status":"EXPIRED","holder":"Demo credential (SAMPLE)"},
    ]
    reg_js=json.dumps(registry)
    page=f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Verify a credential · ChainSentry Academy</title><style>{CSS}</style></head><body>
<header><div class="wrap nav">
  <div class="logo"><div class="logo-mark">◈</div><b>CCA</b><span class="div"></span><small>CHAINSENTRY<br>ACADEMY</small></div>
  <nav class="links">{nav_html(None)}</nav>
  <div class="lang-pill"><span>🌐</span> EN</div>
  <a class="btn btn-gold" href="#">Sign in</a>
</div></header>
<div class="hero" style="padding:44px 0"><div class="ghost" aria-hidden="true">✓</div><div class="wrap">
  <div class="crumb">HOME / <b>VERIFY</b></div>
  <h1 style="font-size:44px">Verify a credential</h1>
  <p class="sub">Enter a credential ID exactly as printed. Verification is performed against the Academy registry.</p>
</div></div>
<div class="wrap" style="max-width:760px;padding:40px 24px 80px">
  <div class="card">
    <div class="micro side-label">CREDENTIAL ID</div>
    <div style="display:flex;gap:12px;margin-top:8px">
      <input id="qid" class="vin" placeholder="CCA-XXX-YYYY-NNNN" spellcheck="false">
      <button class="btn btn-gold" onclick="verify()">Verify</button>
    </div>
    <p class="note" style="margin-top:12px">Demo registry IDs to try: <span class="mono">CCA-BTE-2026-0042</span> · <span class="mono">CCA-CAP-2026-0117</span> · <span class="mono">CCA-CTX-2026-0008</span></p>
    <div id="result" style="margin-top:8px"></div>
  </div>
</div>
<script>
const REG={reg_js};
function renderRow(k,v,cls){{return `<div class="defrow"><span class="dk">${{k}}</span><span class="dv ${{cls||''}}">${{v}}</span></div>`}}
function verify(){{
  const q=document.getElementById('qid').value.trim().toUpperCase();
  const out=document.getElementById('result');
  if(!q){{out.innerHTML='<p class="note">Enter an ID first.</p>';return}}
  const hit=REG.find(r=>r.id.toUpperCase()===q);
  if(!hit){{
    out.innerHTML=`<div class="vres" style="border-color:rgba(226,178,94,.4)">
      <div class="micro">RESULT</div><div class="vbig" style="color:var(--gold-txt)">NOT FOUND</div>
      <p class="note">No credential <span class="mono">${{q}}</span> in the registry. Check the ID and try again.</p></div>`;
    return;
  }}
  const ok=hit.status==="VALID";
  out.innerHTML=`<div class="vres" style="border-color:${{ok?'var(--green-border)':'rgba(226,178,94,.5)'}}">
    <div class="micro">RESULT — ${{hit.status}}</div>
    <div class="vbig" style="color:${{ok?'var(--green)':'var(--gold-txt)'}}">${{ok?'VALID':'EXPIRED'}}</div>
    <div class="deflist" style="margin-top:12px">
      ${{renderRow('Credential ID',hit.id)}}
      ${{renderRow('Course',hit.course)}}
      ${{renderRow('Issued',hit.issued)}}
      ${{renderRow('Expires',hit.expires)}}
      ${{renderRow('Registry', 'CCA mainnet registry · demo dataset')}}
    </div></div>`;
}}
document.getElementById('qid').addEventListener('keydown',e=>{{if(e.key==='Enter')verify()}});
const qp=new URLSearchParams(location.search).get('id');
if(qp){{document.getElementById('qid').value=qp;verify()}}
</script>
<style>
.vin{{flex:1;background:var(--panel2,#0E1626);border:1px solid var(--border);border-radius:8px;color:var(--txt);padding:11px 14px;font-family:var(--mono);font-size:14px}}
.vin:focus{{outline:none;border-color:var(--gold-border)}}
.vres{{border:1px solid var(--border);border-radius:12px;padding:20px 22px;margin-top:16px;background:rgba(255,255,255,.015)}}
.vbig{{font-size:30px;font-weight:700;margin-top:4px}}
.defrow{{display:flex;justify-content:space-between;padding:9px 0;border-bottom:1px solid var(--border);font-size:14px}}
.defrow:last-child{{border-bottom:none}}.dk{{color:var(--mut)}}.dv{{font-weight:500}}
</style>
{FOOT}"""
    open(OUT+"cca-academy-verify.html","w").write(page)

# generate all
made=[course_page(k,v) for k,v in COURSES.items()]
hub_page(); verify_page()
manifest={"generated":datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
          "files":sorted(made)+["cca-academy-index.html","cca-academy-verify.html"],
          "courses":{k:{**v,"cert":CERT_META[k]} for k,v in COURSES.items()},
          "template_owner":"scripts/gen-academy.py (canonical)"}
json.dump(manifest, open(OUT+"academy-manifest.json","w"), indent=2)
for f in manifest["files"]:
    print(f"  ✓ {f:42s} {os.path.getsize(OUT+f):7d}B")
print("\nGENERATED", len(manifest["files"]), "pages")
#!/usr/bin/env python3
"""PDF twin of the management-review DOCX (same machine-extracted data)."""
import json, html, re
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.colors import HexColor, white
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.enums import TA_LEFT

DATA = json.load(open("/home/mtadmin/.hermes/cache/cs-gap-extract.json"))
OUT = "/home/mtadmin/.hermes/intel/chainsentry-pipeline/reports/ChainSentry-Product-Gaps-Management-Review-20261028.pdf"
NAVY, GREY = HexColor("#1F3864"), HexColor("#666666")
tier_color = {"Critical": HexColor("#C00000"), "Must": HexColor("#BF8F00"), "Should": HexColor("#2E74B5"), "Future": HexColor("#7F7F7F")}

def P(text, size=10.5, bold=False, color=None, space=6, bullet=False, lead=13.5):
    txt = html.escape(text)
    txt = txt.replace("&amp;#", "&#")  # restore intentional numeric entities after escaping
    if "**" in text:
        parts = html.escape(text).split("**")
        txt = "".join(f"<b>{c}</b>" if i % 2 else c for i, c in enumerate(parts))
    if bullet: txt = "&#8212;&nbsp;&nbsp;" + txt
    st = ParagraphStyle("p", fontName="Helvetica-Bold" if bold else "Helvetica", fontSize=size,
                        leading=lead, spaceAfter=space, textColor=color or HexColor("#111111"), alignment=TA_LEFT)
    return Paragraph(txt, st)

def H(text, size=13):
    return P(text, size=size, bold=True, color=NAVY, space=5)

doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=18*mm, rightMargin=18*mm, topMargin=18*mm, bottomMargin=18*mm)
el = []
el.append(P("chain:SENTRY", size=19, bold=True, color=NAVY, space=2))
el.append(P("Product Documentation Gaps &#8212; Management Review &amp; Funding Baseline", size=13, bold=True, space=2))
el.append(P("Compiled 28 October 2026 (MYT) &#183; v1.0 &#183; CONFIDENTIAL &#8212; internal management review", size=8.5, color=GREY, space=8))
el.append(HRFlowable(width="100%", thickness=0.7, color=NAVY, spaceAfter=9))

el.append(H("1. Announcement-Ready Abstract (for the funding request)"))
abstract = ("chain:SENTRY, Aras Integrasi's sovereign blockchain-investigation platform, has completed its first "
 "law-enforcement briefing cycle: PDRM CCID/JSJK Forensik received the full product briefing on 27 October 2026, an adoption "
 "decision is pending, and a government evaluation channel (CyberSecurity Malaysia) opens with a confirmed 11 November "
 "leadership meeting. The platform's verified core is strong &#8212; 26/26 page routes and 32/32 authenticated API paths returned "
 "live data under independent verification, backed by a 583,574-tag attribution corpus across 78 chains and sanctions "
 "screening at sub-20-millisecond latency. Thirteen documented work packages separate this verified core from pilot "
 "delivery: 4 critical, 3 must-have, 4 should-have, 2 future. The immediate funding need is delivery capacity &#8212; the adopted "
 "7-FTE operating model (CC-01 envelope MYR 100&#8211;150k/month) remains unfilled and a 2-engineer span of responsibility now "
 "gates three concurrent government adoption tracks. Positioning is not verification: no external capability claim is made "
 "beyond the evidence base cited herein.")
el.append(P(abstract, space=10))

el.append(H("2. Readiness Verdict (spec-evidenced)"))
el.append(P("Not ready for production/GA &#8212; pilot scope only, after Phase 0. [T2, spec &#167;5.2&#8211;5.4]", bold=True, space=4))
for b in ["Deployment parity: 22-commit / 32-day development-to-deployment lag (TEC-012) &#8212; release risk accumulates daily.",
 "External access: service unreachable externally; named pilot accounts not issued; session URL requires correction (BLK-002/003).",
 "Credential closure: four provider keys previously exposed; rotation outstanding (BLK-001). C1 recorded closed on operator confirmation 8 Sep; evidence item (fingerprint record) remains open in the C2 pack.",
 "Live-vs-demo boundary: a 31-tool registry remains fixture-backed while the dossier registry is live (DEF-009) &#8212; no pilot result may be fixture data.",
 "Governance context: reduced-screening interim posture per DAF Option B ruling 26 Oct (DEC-20261026-001); consolidated Phase-0 (M2&#8211;M7) status report due 2 Nov 2026 (ACT-20261026-002)."]:
    el.append(P(b, bullet=True, space=3))
el.append(Spacer(1, 6))

el.append(H("3. Verified Strengths (the asset being funded)"))
for b in ["Verification sweep: 26/26 page routes correct; 32/32 authenticated GET paths returned live data; 44 API handlers in the recorded baseline.",
 "Risk discrimination confirmed: exchange 16/Minimal; OFAC-listed 90/Critical; mixer router 65/High.",
 "Measured performance (warm): screening/attribution &lt;20 ms; trace-to-cash-out ~32 s; composite score 1.4&#8211;1.5 s.",
 "Attribution corpus: 583,574 tags / 524,656 addresses / 78 chains; sanctions registry 4,633 addresses; 1,790 checksum-verified dark-web contributions labelled 'observed' &#8212; never criminal attribution.",
 "Commercial layer registered: editions-only SKU catalog (Professional RM 96k/yr &#183; Enterprise RM 348k/yr; reference deals RM 698k and RM 300k Y1)."]:
    el.append(P(b, bullet=True, space=3))
el.append(Spacer(1, 6))

el.append(H("4. Gap Register &#8212; 13 Documented Work Packages"))
el.append(P("Extracted programmatically from MVP Specification v3.0 priority gap matrix (&#167;5.4.1); remediation phrasing condensed from the spec's resolution column.", size=8.5, color=GREY, space=5))
rows = [[P("Tier", size=9, bold=True, color=white), P("Work package", size=9, bold=True, color=white), P("Ref IDs", size=9, bold=True, color=white), P("What closing it delivers", size=9, bold=True, color=white)]]
for r in DATA["gap_matrix"]:
    ids = ", ".join(r["gap_ids"]) if r["gap_ids"] else "(contract parity)"
    res = r["resolution"] if len(r["resolution"]) <= 230 else r["resolution"][:227].rstrip() + "..."
    rows.append([P(r["priority"], size=8.5, bold=True, color=white), P(r["area"], size=8.5), P(ids, size=8.5), P(res, size=8.5)])
t = Table(rows, colWidths=[20*mm, 47*mm, 27*mm, 82*mm], repeatRows=1)
style = [("BACKGROUND", (0,0), (-1,0), NAVY), ("GRID", (0,0), (-1,-1), 0.4, HexColor("#9AA5B1")),
         ("VALIGN", (0,0), (-1,-1), "TOP"), ("ROWBACKGROUNDS", (0,1), (-1,-1), [white, HexColor("#F4F6FA")])]
for i, r in enumerate(DATA["gap_matrix"], start=1):
    style.append(("BACKGROUND", (0,i), (0,i), tier_color.get(r["priority"], white)))
t.setStyle(TableStyle(style))
el.append(t); el.append(Spacer(1, 8))

el.append(H("5. Funding Structure (three tranches)"))
for b in ["Tranche 1 &#8212; Pilot-critical (immediate). The 4 Critical + 3 Must packages: release reconciliation, external TLS + named accounts, credential rotation, truth boundary, API contract regeneration, source-role renewal, blocking quality gates. This tranche is the gate to the Phase-1 exit criterion &#8212; a partner-agency investigator completing a case intake-to-report on live intelligence. It unblocks the stalled first government evaluation (testing-access action open since 15 Oct) and directly serves the pending PDRM adoption decision.",
 "Tranche 2 &#8212; Productisation. The 4 Should packages: migration runner + tested backup/restore, second-tenant isolation and quotas, batch screening + signed PDF exports + audit UI, email alerting and observability. These convert a verified pilot into a defensible multi-agency service.",
 "Tranche 3 &#8212; Capability expansion (roadmap). The 2 Future packages: non-EVM tracing beginning with Bitcoin (the PDRM-relevant USDT/Tron line rides the same work), and cryptographically signed, fully-provenanced evidence dossiers &#8212; the court-grade assurance tier.",
 "Capacity basis: funding is requested against the adopted 7-FTE operating model (CC-01 envelope MYR 100&#8211;150k/month, DEC-20260908-001). The binding constraint is not technology &#8212; all 13 packages are documented engineering work against an already-verified core &#8212; but hands: a 2-FTE technical unit currently spans three products. The chain:SENTRY hiring exception remains dormant by ruling; this review is the vehicle to activate it."]:
    el.append(P(b, bullet=True, space=4))
el.append(Spacer(1, 4))

el.append(H("6. Risk if Unfunded"))
for b in ["Adoption gates open before readiness: PDRM decision (imminent), CSM evaluation (11 Nov anchor), panel launch (composition-gated) &#8212; all three can arrive while the product remains pilot-blocked and externally unreachable.",
 "Single point of failure compounds: one engineer carrying deployment parity, security remediation (7 open findings from the 23 Oct full-zone scan) and two sibling products.",
 "Hiring window already lapsed: the Oct 13&#8211;20 start window expired unused; every week of delay compounds post-expiry disposition debt and pushes pilot readiness into Q1 2027.",
 "Competitive window: PDRM is actively shopping for blockchain-detection tooling (incumbent China-sourced; prior exposure to TRM Labs, Chainalysis, Crystal, Uppsala). A funded sovereign-local alternative meets a live procurement gap; an unfunded one watches it close."]:
    el.append(P(b, bullet=True, space=3))
el.append(Spacer(1, 6))

el.append(H("7. Methodology &amp; Sources"))
for b in ["Gap register machine-extracted from products/chainsentry/MVP_SPECIFICATION.md (MVP Product Specification v3.0, registered DOC-20260814-001) &#8212; 13 rows, 13/13 baseline figures verified at extraction.",
 "Commercial figures from SKU Catalog v3.0 (DOC-20260924-010). Governance state from DEC-20261026-001, ACT-20261026-002, AIP Gate Tracker (28 Oct check). Adoption posture from CONV-20261028-004 (CCID/JSJK) and EVT-20261027-001 (CSM 11 Nov).",
 "Claim discipline: positioning &#8800; verification; no capability claim beyond the cited evidence base; Solana/coverage phrasing corrected to 'attribution + sanctions (tracing: EVM only)' per spec &#167;6 boundaries."]:
    el.append(P(b, bullet=True, space=3))

doc.build(el)
print("saved", OUT)

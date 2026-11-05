#!/usr/bin/python3
"""Jeffri Ashari decision brief - PDF. Alignment-critical: figures from the JSON, not retyped."""
import html, re, json
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib.colors import HexColor

SRC = "/home/mtadmin/.hermes/intel/chainsentry-pipeline/strategy/JEFFRI-DECISION-BRIEF-20261105.json"
OUT = "/home/mtadmin/.hermes/intel/chainsentry-pipeline/strategy/JEFFRI-DECISION-BRIEF-20261105.pdf"
D = json.load(open(SRC))

NAVY = HexColor("#12263F"); ACCENT = HexColor("#B3261E"); GREY = HexColor("#5A6672")
LIGHT = HexColor("#F2F4F7"); RULE = HexColor("#D5DBE1"); GREEN = HexColor("#1E6B3A")

ss = getSampleStyleSheet()
H1 = ParagraphStyle("H1", parent=ss["Heading1"], fontName="Helvetica-Bold", fontSize=16, textColor=NAVY, leading=19, spaceAfter=4)
H2 = ParagraphStyle("H2", parent=ss["Heading2"], fontName="Helvetica-Bold", fontSize=11.5, textColor=NAVY, spaceBefore=11, spaceAfter=4, leading=14)
BODY = ParagraphStyle("BODY", parent=ss["BodyText"], fontName="Helvetica", fontSize=9.2, leading=12.8, alignment=TA_JUSTIFY, textColor=HexColor("#1A1A1A"), spaceAfter=5)
BUL = ParagraphStyle("BUL", parent=BODY, leftIndent=11, bulletIndent=2, spaceAfter=2.6, alignment=TA_LEFT)
CAP = ParagraphStyle("CAP", parent=BODY, fontName="Helvetica-Oblique", fontSize=7.6, textColor=GREY, spaceAfter=7, leading=9.6, alignment=TA_LEFT)
CELL = ParagraphStyle("CELL", parent=BODY, fontSize=8.2, leading=10.6, spaceAfter=0, alignment=TA_LEFT)
TH = ParagraphStyle("TH", parent=CELL, fontName="Helvetica-Bold", textColor=colors.white)

def P(t, s=BODY):
    t = str(t)
    t = t.replace("<b>", "\x01B\x01").replace("</b>", "\x01/B\x01")
    t = t.replace("<i>", "\x01I\x01").replace("</i>", "\x01/I\x01")
    t = html.escape(t)
    t = t.replace("\x01B\x01", "<b>").replace("\x01/B\x01", "</b>")
    t = t.replace("\x01I\x01", "<i>").replace("\x01/I\x01", "</i>")
    for pat, rep in [(r"\*\*(.+?)\*\*", r"<b>\1</b>")]:
        t = re.sub(pat, rep, t)
    return Paragraph(t, s)

def esc_cell(t):
    t=str(t)
    t=t.replace("<b>","\x01B\x01").replace("</b>","\x01/B\x01").replace("<i>","\x01I\x01").replace("</i>","\x01/I\x01")
    t=html.escape(t)
    return t.replace("\x01B\x01","<b>").replace("\x01/B\x01","</b>").replace("\x01I\x01","<i>").replace("\x01/I\x01","</i>")

def table(header, rows, widths, shade=None, caption=None):
    data=[[Paragraph(esc_cell(h), TH) for h in header]]
    for r in rows:
        data.append([Paragraph(esc_cell(c), CELL) for c in r])
    t=Table(data, colWidths=widths, repeatRows=1)
    st=[("BACKGROUND",(0,0),(-1,0),NAVY),("GRID",(0,0),(-1,-1),0.4,RULE),("VALIGN",(0,0),(-1,-1),"TOP"),
        ("LEFTPADDING",(0,0),(-1,-1),4.5),("RIGHTPADDING",(0,0),(-1,-1),4.5),
        ("TOPPADDING",(0,0),(-1,-1),3.4),("BOTTOMPADDING",(0,0),(-1,-1),3.4)]
    if shade: st.append(("ROWBACKGROUNDS",(0,1),(-1,-1),shade))
    t.setStyle(TableStyle(st))
    out=[t]
    if caption: out.append(P(caption, CAP))
    return [KeepTogether(out)]

story=[]
story.append(P("CONFIDENTIAL — INTERNAL DECISION BRIEF", CAP))
story.append(Spacer(1, 3*mm))
story.append(P("Decision Brief — Hire Jeffri Ashari", H1))
story.append(P("Head of Financial Crime Compliance (candidate) · FIT=HIGH / HIRE-VERIF=PENDING · prepared 5 November 2026", CAP))

# verdict box
vb=Table([[Paragraph("<b>RECOMMENDATION.</b> Hire — <b>full-time</b>, not advisor retainer — conditional on two "
    "verifications: independent corroboration of the resume, and referee identity resolution. "
    "<b>The asymmetry:</b> downside is one salary inside a 7-FTE plan already ratified; upside is the trust "
    "apparatus for P3 regulator packaging, warm access to uncontested BNM-orbit segments, and a defensible "
    "answer to the only question that kills enterprise sales — <i>\u201csays who?\u201d</i>", BODY)]],
    colWidths=[168*mm])
vb.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),LIGHT),("BOX",(0,0),(-1,-1),0.8,NAVY),
    ("LEFTPADDING",(0,0),(-1,-1),7),("RIGHTPADDING",(0,0),(-1,-1),7),
    ("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6)]))
story.append(vb); story.append(Spacer(1,4*mm))

story.append(P("1. Why Him — The Business Logic", H2))
story.append(P("<b>BLUF.</b> ChainSentry sells AML/CFT tooling into rooms where we hold no native credibility, "
    "and the product's entire value proposition is <b>court-grade trust</b>. Jeffri is the buyer persona we are "
    "selling to: a 10-year financial-intelligence practitioner from inside the exact institutional world — "
    "BNM-regulated banking, STR filing, takaful, KYC/CDD — that constitutes the addressable market. Hiring him "
    "converts the hardest sales problem (<i>why should a compliance head trust a startup's forensics output?</i>) "
    "into an internal capability. This is not a hire; it is a market-entry asset wearing a payroll number.", BODY))

story += table(["#", "Pillar", "Fact base", "Benefit to ChainSentry"],
  [[str(i+1), p["pillar"], p["facts"], p["benefit"]] for i,p in enumerate(D["business_case"])],
  [7*mm, 34*mm, 60*mm, 67*mm], shade=[colors.white, LIGHT],
  caption="Table 1 — Six-pillar business case. Facts are self-reported pending verification (discipline stated in header).")

story.append(PageBreak())
story.append(P("2. Market Timing — Why Now", H2))
story.append(P("KL's crypto-AML buying cluster is hiring <b>now</b>. Bybit posted six AML/crypto-risk roles in "
    "Greater KL naming Chainalysis, Elliptic, TRM Labs and CipherTrace verbatim — the incumbent stack is being "
    "specified in job descriptions, which means displacement windows are observable. TNG Digital posted a "
    "department-head Financial Crime Compliance role with <b>no incumbent tool named</b> — a 6\u201312 month "
    "purchase window that opens from their hire date. Whoever holds that seat at TNG will speak fluent "
    "Jeffri. So should we.", BODY))
story.append(P("<b>The buying-centre map [INT-20261010-002, HIGH]:</b> AML purchasing authority in the KL cluster "
    "sits with compliance departments, not engineering. First Digital = greenfield compliance ops; StraitsX/Monee "
    "= institutional scaling pair; Deloitte KL = channel signal. Every one of these conversations is shorter "
    "when the person on our side of the table has written the artifacts their side produces.", BODY))

story.append(P("3. What His Expertise Buys — Sequenced Against the AMLA Plan", H2))
story += table(["Plan stage", "Commercial milestone", "What Jeffri adds"],
  [["P0","BridgeHold Evidence Pack (HyperUnit failed-custody case as lighthouse demo)","Compliance framing of a bridge failure — an ML/ATF story, not an engineering anecdote"],
   ["P1","Holder-cohort registry (user-gated)","Corpus-integrity judgment: what is admissible, what is hygiene"],
   ["P2","'Explainable-Hold' pilot","Design input on the artifact examiners will actually accept"],
   ["P3","Regulator packaging — BNM-FIED / SC / CCID (counsel-gated)","Fluency in exactly what FIED expects from a filer; the commercial summit"],
  ], [16*mm, 74*mm, 78*mm], shade=[colors.white, LIGHT],
  caption="Table 2 — The four-stage AMLA plan. P3 is unreachable without practitioner-grade compliance fluency; this is the hiring rationale in one row.")

story.append(P("4. Engineered Success Metrics (already encoded in the JD)", H2))
m=D["engineered_success_metrics"][0]
story += table(["Day 30","Day 90","Month 12"],
  [[m["day30"], m["day90"], m["month12"]]],
  [52*mm, 60*mm, 56*mm],
  caption="Success is defined as named product-trust artifacts, not activity. His success mechanically produces the trust apparatus ChainSentry sells on.")

story.append(P("5. Conditions, Guardrails and Open Calls", H2))
story += table(["Item","State"],
  [["<b>HIRE-VERIF</b>","PENDING — fit graded from self-report; external corroboration of resume claims must be rerun before any offer [record INT-20261015-001]"],
   ["<b>Referee identity</b>","CONFLICT FLAGGED — Muhammad Fadhli (Head of Compliance, ShopeePay|SeaMoney MY) shares a name with MX Global's verified contact fadzli@mxglobal.com.my; employer attribution unresolved — resolve before approach"],
   ["<b>Guardrails</b>","No current-employer solicitation; no year-1 quota commitments; independence note intact"],
   ["<b>Owner call 1</b>","FT vs 2-day advisor retainer — open since 15 Oct; recommendation: FT if P3/BNM\u2013SC engagement is on the 12-month horizon (retainer savings evaporate in coordination cost)"],
   ["<b>Owner call 2</b>","Salary band confirmation — blocks ACT-20261008-002 prong 1 (posting with confirmed grade and band); the ACT is 14 days overdue"],
   ["<b>Owner call 3</b>","Posting channels — LinkedIn / HRT2U-CareersHub MY / CAMA-ACAMS MY network / Big-4 forensic referral"],
   ["<b>Screen design</b>","Writing sample + live public-cluster tracing exercise + data-rights clause negotiation instinct — designed, not yet run"],
  ], [30*mm, 138*mm], shade=[colors.white, LIGHT],
  caption="Table 3 — Decision dependencies. None are technical; all three open calls are owner-side.")

story.append(P("6. Basis and Discipline", H2))
for b in ["Candidate record INT-20261015-001 (FIT=HIGH / HIRE-VERIF=PENDING; resume self-reported 15 Oct via operator DM).",
          "Hiring ACT-20261008-002 (P1, due 2026-10-22, in-progress, 14 days overdue as of 5 Nov).",
          "Buying-cluster intelligence INT-20261010-002 (Bybit/TNG/First Digital/StraitsX/Deloitte posting evidence, LinkedIn jobs-guest API).",
          "Activation suite ART-20260908-002 family and DEC-20260908-001 (7-FTE model the salary sits inside).",
          "Resume facts are <b>[SELF-REPORTED]</b> and marked; no claim in this brief extends beyond the register. No defamation risk carried: the brief assesses fit, not the person.",
          "This document is an internal decision aid, not investment or legal advice."]:
    story.append(P("\u2022 " if False else "\u2014 " + b, BUL))

def deco(canv, doc):
    canv.saveState(); canv.setStrokeColor(RULE); canv.setLineWidth(0.5)
    canv.line(20*mm, 15*mm, 190*mm, 15*mm)
    canv.setFont("Helvetica", 7); canv.setFillColor(GREY)
    canv.drawString(20*mm, 10.5*mm, "Decision Brief — Jeffri Ashari, Head FCC (candidate)")
    canv.drawRightString(190*mm, 10.5*mm, f"Page {doc.page}")
    canv.restoreState()

doc=SimpleDocTemplate(OUT, pagesize=A4, leftMargin=20*mm, rightMargin=20*mm, topMargin=18*mm, bottomMargin=18*mm,
    title="Decision Brief - Hire Jeffri Ashari, Head of Financial Crime Compliance",
    author="Vesper / Aras Integrasi", subject="Hiring decision brief")
doc.build(story, onFirstPage=deco, onLaterPages=deco)
print("BUILT:", OUT)

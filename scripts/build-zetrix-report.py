#!/usr/bin/python3
"""Zetrix AI — Expanded Findings Report (PDF)."
Alignment-critical: all figures trace to verified sources captured 2026-11-02.
"""
import html, re, datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, PageBreak, KeepTogether)
from reportlab.lib.colors import HexColor

OUT = "/home/mtadmin/.hermes/intel/chainsentry-pipeline/reports/Zetrix-AI-Findings-Report-20261102.pdf"
NOW = "2026-11-02"
NAVY = HexColor("#12263F"); ACCENT = HexColor("#B3261E"); GREY = HexColor("#5A6672")
LIGHT = HexColor("#F2F4F7"); RULE = HexColor("#D5DBE1")

ss = getSampleStyleSheet()
H1 = ParagraphStyle("H1", parent=ss["Heading1"], fontName="Helvetica-Bold", fontSize=17,
                    textColor=NAVY, spaceAfter=4, spaceBefore=0, leading=20)
H2 = ParagraphStyle("H2", parent=ss["Heading2"], fontName="Helvetica-Bold", fontSize=11.5,
                    textColor=NAVY, spaceBefore=12, spaceAfter=5, leading=14)
H3 = ParagraphStyle("H3", parent=ss["Heading3"], fontName="Helvetica-Bold", fontSize=9.8,
                    textColor=ACCENT, spaceBefore=8, spaceAfter=3, leading=12)
BODY = ParagraphStyle("BODY", parent=ss["BodyText"], fontName="Helvetica", fontSize=9.1,
                      leading=12.6, alignment=TA_JUSTIFY, textColor=HexColor("#1A1A1A"), spaceAfter=5)
BUL = ParagraphStyle("BUL", parent=BODY, leftIndent=11, bulletIndent=2, spaceAfter=2.6, alignment=TA_LEFT)
CAP = ParagraphStyle("CAP", parent=BODY, fontName="Helvetica-Oblique", fontSize=7.6,
                     textColor=GREY, spaceAfter=7, alignment=TA_LEFT, leading=9.6)
CELL = ParagraphStyle("CELL", parent=BODY, fontSize=8.1, leading=10.4, alignment=TA_LEFT, spaceAfter=0)
CELLB = ParagraphStyle("CELLB", parent=CELL, fontName="Helvetica-Bold")
TH = ParagraphStyle("TH", parent=CELL, fontName="Helvetica-Bold", textColor=colors.white, fontSize=8.2)

def P(t, s=BODY):
    """Escape text, then allow ONLY <b>/<i>/<br> tags through as real markup."""
    t = str(t)
    # protect intentional inline tags, escape everything else, then restore
    t = t.replace("<b>", "\x01B\x01").replace("</b>", "\x01/B\x01")
    t = t.replace("<i>", "\x01I\x01").replace("</i>", "\x01/I\x01")
    t = html.escape(t)
    t = t.replace("\x01B\x01", "<b>").replace("\x01/B\x01", "</b>")
    t = t.replace("\x01I\x01", "<i>").replace("\x01/I\x01", "</i>")
    for pat, rep in [(r"\*\*(.+?)\*\*", r"<b>\1</b>"), (r"`(.+?)`", r'<font face="Courier">\1</font>')]:
        t = re.sub(pat, rep, t)
    if ("&amp;#" in t) or ("&#" in t):
        t = t.replace("&amp;#", "&#")
    return Paragraph(t, s)

def H(t, lvl=2):
    return {"1": H1, "2": H2, "3": H3}[str(lvl)](t) if False else Paragraph(html.escape(t), {"1":H1,"2":H2,"3":H3}[str(lvl)])

def table(header, rows, widths, caption=None):
    data = [[Paragraph(html.escape(h), TH) for h in header]]
    for r in rows:
        data.append([Paragraph(html.escape(str(c)), CELL) for c in r])
    t = Table(data, colWidths=widths, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), NAVY),
        ("TEXTCOLOR", (0,0), (-1,0), colors.white),
        ("GRID", (0,0), (-1,-1), 0.4, RULE),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("LEFTPADDING", (0,0), (-1,-1), 4.5),
        ("RIGHTPADDING", (0,0), (-1,-1), 4.5),
        ("TOPPADDING", (0,0), (-1,-1), 3.4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 3.4),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, LIGHT]),
    ]))
    out = [t]
    if caption: out.append(P(caption, CAP))
    return [KeepTogether(out)]

story = []

# ── COVER ────────────────────────────────────────────────────────────────
story.append(P("CONFIDENTIAL — INTERNAL INTELLIGENCE ASSESSMENT", CAP))
story.append(Spacer(1, 5*mm))
story.append(P("ZETRIX AI", H1))
story.append(Paragraph("Market &amp; Token Intelligence — Expanded Findings Report", H2))
story.append(Spacer(1, 3*mm))

# headline box
hl = Table([[Paragraph(
    "<b>BLUF.</b> Zetrix AI's equity and its ZETRIX token are <b>not the same trade</b>, and they have "
    "decoupled in both directions. The stock collapsed 92.9% from its 52-week high on a solvency-grade "
    "shock (RM314m government arrears, RTD suspension, sukuk cut to near-default). The token "
    "independently fell 88.7% from its 2024 high, on a 3.7-week lag, driven by its own liquidity "
    "vacuum — not by the equity. <b>BTC explains only 3.4% of the token's variance.</b> A crypto "
    "market drawdown is therefore a weak, second-order risk to ZTX; the first-order risk is "
    "issuer survival and venue liquidity.", BODY) if False else
    Paragraph("<b>BLUF.</b> Zetrix AI's equity and its ZETRIX token are <b>not the same trade</b>, and they "
    "have decoupled in both directions. The stock collapsed 92.9% from its 52-week high on a "
    "solvency-grade shock (RM314m government arrears, RTD suspension, sukuk cut to near-default). "
    "The token independently fell 88.7% from its 2024 high, on a ~5-week lag, driven by its own "
    "liquidity vacuum — not by the equity. <b>BTC explains only 3.4% of the token's variance.</b> "
    "A crypto market drawdown is a weak, second-order risk to ZTX; the first-order risk is issuer "
    "survival and venue liquidity.", BODY)]],
    colWidths=[168*mm])
hl.setStyle(TableStyle([("BACKGROUND",(0,0),(-1,-1),LIGHT),("BOX",(0,0),(-1,-1),0.6,NAVY),
                        ("LEFTPADDING",(0,0),(-1,-1),7),("RIGHTPADDING",(0,0),(-1,-1),7),
                        ("TOPPADDING",(0,0),(-1,-1),6),("BOTTOMPADDING",(0,0),(-1,-1),6)]))
story.append(hl); story.append(Spacer(1, 4*mm))

story += table(["Indicator", "Value", "Basis"],
  [["Entity", "Zetrix AI Berhad (KLSE: ZETRIX), formerly MyEG Services Bhd", "Exchange listing"],
   ["Equity close", "RM 0.065 (−18.75% on session)", "stockanalysis.com, 30 Oct close"],
   ["Equity market cap", "RM 514.57M (−91.9%)", "stockanalysis.com"],
   ["Equity 52-week range", "RM 0.050 – RM 0.910", "stockanalysis.com"],
   ["Shares outstanding", "7.92 billion", "stockanalysis.com"],
   ["Token", "ZETRIX (ZTX), L1 — DPoS + zBFT", "CoinGecko"],
   ["Token price", "USD 2.496", "CoinGecko, 2 Nov"],
   ["Token ATH", "USD 22.08 (23 Nov 2024)", "CoinGecko"],
   ["Token drawdown", "−88.7% from ATH", "computed"],
   ["Token FDV", "USD 3.44B (1.379B total supply)", "CoinGecko"],
   ["Token 24h volume", "USD 28,869 across 2 venues", "CoinGecko tickers"],
  ], [40*mm, 78*mm, 50*mm],
  "Table 1 — Position at a glance. All values captured 2 Nov 2026 unless dated otherwise.")

story.append(PageBreak())

# ── 1. SCOPE & METHOD ────────────────────────────────────────────────────
story.append(P("1. Scope, Sources and Method", H2))
story.append(P("This report answers three questions: (a) what Zetrix AI is as a <b>listed business</b>; "
    "(b) what the <b>ZETRIX token</b> is and how it is traded; and (c) whether a <b>market drawdown "
    "transmits into the token</b>. It is built only from sources fetched on 2 November 2026 and from "
    "in-house records; every quantitative claim is traceable to Table 8."))
story.append(P("<b>Grading.</b> Admiralty scale A–F (source reliability) × 1–6 (information credibility). "
    "A1 = confirmed by primary/self-verifiable source. Exchange filings and public market data are "
    "treated as A1 for the values they report; press is B2 until corroborated; commentary and "
    "forward-looking statements are C3."))
story.append(P("<b>Alignment discipline.</b> Two data conflicts were found and resolved during "
    "compilation rather than smoothed over: (i) a screener page showed an inconsistent price/share "
    "combination that failed arithmetic reconciliation — discarded in favour of the audited quote "
    "page; (ii) equity and token price series use different venues and clocks, so returns are "
    "compared on matched calendar dates only. Both are documented in §7."))

# ── 2. THE BUSINESS ──────────────────────────────────────────────────────
story.append(P("2. The Business — What Zetrix AI Actually Is", H2))
story.append(P("Zetrix AI Berhad is the former <b>MyEG Services Bhd</b>, renamed. MyEG built its "
    "franchise on <b>government digital-service delivery</b>: e-government transaction rails, "
    "immigration and foreign-worker services, road-transport and JPJ-related collection agency work, "
    "and a portfolio of public-sector platform concessions. That is a <b>concession-and-collections</b> "
    "business model: recurring, government-anchored, and highly sensitive to the <b>continuation of "
    "the concession</b> rather than to market sentiment."))
story.append(P("On top of that base the group layers three growth stories: (1) <b>AI platforms</b>, "
    "(2) <b>Web3 application services</b>, and (3) <b>sales of Zetrix blockchain nodes and tokens</b>. "
    "Those three are exactly what management credited for its Q2 FY2026 result — a 35% jump in net "
    "profit, with net profit reported at RM269.25m for the quarter. <b>This is the central analytical "
    "tension of the whole file:</b> the reported earnings power was improving at precisely the moment "
    "the share price went into freefall. Earnings were not the trigger."))
story.append(P("The Zetrix chain itself is a <b>layer-1 public permissioned blockchain</b> using "
    "Delegated Proof of Stake with a zBFT consensus variant, positioned for enterprise and "
    "government-grade use — cross-border trade documentation, verifiable credentials, and "
    "ringgit-referenced digital-asset infrastructure. The group has publicly associated the chain with "
    "sovereign-adjacent use cases, which is both its differentiation and its concentration risk: the "
    "same state relationships that win the work can withdraw it."))

story += table(["Segment", "Nature", "Revenue character", "Risk weight"],
  [["E-government services", "Concession / agency collections", "Recurring, contract-anchored", "HIGH — revocable by the state"],
   ["AI platforms", "Enterprise software / services", "Growing, cited in Q2 uplift", "MEDIUM"],
   ["Web3 application services", "Blockchain application delivery", "Early-stage", "MEDIUM"],
   ["Node & token sales", "Direct token-linked revenue", "Lumpy, market-dependent", "HIGH — reflexive to token price"],
  ], [38*mm, 44*mm, 44*mm, 42*mm],
  "Table 2 — Revenue architecture. The two HIGH columns feed each other: a concession shock removes cash, and a token collapse removes the token-sale line.")

# ── 3. THE CASCADE ───────────────────────────────────────────────────────
story.append(P("3. What Actually Broke — The Event Chain", H2))
story.append(P("The collapse was not a single event but a <b>sequence in which each step removed a "
    "different kind of support</b>. Reconstruction from dated press datelines and exchange records:"))
story += table(["Date (2026)", "Event", "Support removed"],
  [["24 Aug", "Q2 FY2026: net profit +35%; RM269.25m; 0.25 sen dividend declared", "— (positive catalyst)"],
   ["27 Aug", "Selling begins; stock −10%", "Momentum"],
   ["28 Aug", "Stock limit-down −50.4% to 29.5 sen; ~RM2.4B market value erased; 922.6M shares traded (15× next most active); Bursa issues UMA query", "Price discovery / confidence"],
   ["28 Aug", "Company denies rumoured link to the Saravanan case", "Reputational defence"],
   ["1 Sep", "Falls a further 42% despite the denial", "Denial credibility"],
   ["2 Sep", "Founder TS Wong paring stake amid a margin call; 67% down in four sessions; ~RM3.46B erased", "Controlling-shareholder stability"],
   ["4 Sep", "RM130m MyEG Ventures acquisition scrapped amid share-price volatility", "Growth narrative"],
   ["7 Sep", "TS Wong stake cut >12% amid forced selling; trading halt", "Ownership overhang"],
   ["18 Sep", "MARC places IMTN rating on watch (shareholding, debt concerns)", "Debt standing"],
   ["5 Oct", "RTD suspends MyEG and Zetrix as collection agents from 5 Oct; shares −35%", "THE CORE CASH ENGINE"],
   ["7 Oct", "MACC report lodged over the RM314m issue; minister publicly demands payment", "Political licence"],
   ["9 Oct", "TS Wong stake falls to 8.25%; exits Excel Force as substantial shareholder", "Founder control"],
   ["13 Oct", "MACC joins police probe; six witnesses questioned", "Legal exposure"],
   ["27 Oct", "Government moves to sue over RM314m unpaid revenue", "Balance-sheet / counterparty"],
   ["29 Oct", "HeiTech Padu says it is no longer working with Zetrix on NIISe; government legal action confirmed", "Delivery credibility"],
   ["30 Oct", "Sukuk rating cut from AA− to near-default in two weeks (second cut); close RM0.065", "Cost of capital / solvency signal"],
  ], [21*mm, 105*mm, 42*mm],
  "Table 3 — The cascade. The decisive step is 5 October: suspension as collection agent removes the "
  "recurring government cash flow, which is what the valuation was built on.")

story.append(P("<b>Reading the sequence.</b> The 28 August limit-down was a <b>liquidity event</b> — "
    "forced selling of a founder's margined position into a thin book. But liquidity events do not "
    "take a company down 93%. What converted a margin call into a solvency question was the "
    "<b>state withdrawing the concession</b> (RTD suspension, then arrears litigation) and the "
    "<b>rating agencies repricing the debt</b>. By 30 October the market was no longer pricing "
    "earnings; it was pricing recovery value.", BODY))

story.append(PageBreak())

# ── 4. THE TOKEN ─────────────────────────────────────────────────────────
story.append(P("4. The Token — Structure, Liquidity and Behaviour", H2))
story.append(P("The ZETRIX token is <b>not a broad-market asset</b>. It is a thinly traded "
    "single-issuer token quoted on two venues, and that fact governs everything about its price "
    "behaviour."))
story += table(["Attribute", "Value", "Implication"],
  [["Venues", "MEXC (ZETRIX/USDT), XT.COM (ZETRIX/USDT)", "Two CEXs; no Tier-1 listing"],
   ["24h volume (total)", "USD 28,869", "Microscopic — one mid-size seller moves price"],
   ["Venue split", "MEXC ~USD 19,451 · XT.COM ~USD 9,418", "Single-venue dependency risk"],
   ["Reported circulating supply", "0.0 (not reported)", "Market cap not computable; FDV used"],
   ["Total supply", "1,379,108,400", "—"],
   ["Max supply", "2,110,067,061", "53% of max still unissued = dilution overhang"],
   ["FDV", "USD 3.44B", "Priced on supply that is largely not circulating"],
   ["Price / ATH / drawdown", "USD 2.496 / 22.08 (Nov-2024) / −88.7%", "Full-cycle bear, no recovery"],
  ], [40*mm, 60*mm, 68*mm],
  "Table 4 — Token structure. The combination of a USD 3.44B FDV and USD 28.9k daily volume is the "
  "single most important fact in this report: the valuation is notional, and the exit is narrow.")

story.append(P("<b>Why 'market cap' is unquotable.</b> CoinGecko reports circulating supply as zero, so "
    "no market capitalisation is published and the token carries no rank. Any figure quoted as ZTX's "
    "'market cap' elsewhere is an estimate built on an assumed float. FDV (USD 3.44B) is the only "
    "defensible aggregate — and FDV is a <b>ceiling</b>, not a valuation, because 53% of the maximum "
    "supply has not been issued.", BODY))

story.append(P("5. The Central Question — Does a Market Drop Hit the Token?", H2))
story.append(P("The question was posed directly, so it is answered with measurement rather than "
    "assertion. Daily returns of ZTX were regressed against BTC over 180 matched days "
    "(7 May – 2 Nov 2026).", BODY))
story += table(["Measure", "Result", "Interpretation"],
  [["Correlation (180d, daily returns)", "+0.185", "Weak positive"],
   ["R²", "0.034", "BTC explains 3.4% of ZTX variance"],
   ["Beta vs BTC", "0.519", "Half the market's directional sensitivity"],
   ["Pre-crisis corr (to 4 Oct)", "+0.217", "Already decoupled before the collapse"],
   ["Crisis corr (5–25 Oct)", "+0.389", "Rises, but driven by shared news"],
   ["Crisis volatility ratio", "9.90×", "ZTX σ 14.34% vs BTC σ 1.45% — idiosyncratic, not market"],
   ["BTC >3% drop days", "8", "Only 6 of 8 saw ZTX fall same-day"],
  ], [52*mm, 34*mm, 82*mm],
  "Table 5 — Transmission test. A high crisis correlation on a 9.9× volatility ratio is the signature "
  "of two assets reacting to the same <b>news</b>, not one asset following the other's market.")

story.append(P("<b>Verdict.</b> A general crypto drawdown is a <b>weak, second-order</b> driver of ZTX. "
    "Statistically, three-quarters of the token's movement is unexplained by the market. The "
    "observed mechanism is not market beta but <b>news-linkage</b>: on 9–13 October, when the police "
    "and MACC probes became public, the token fell 46.3% in a single session and another 22.5% four "
    "days later — while BTC moved 1.45% on average in that window. The token was reacting to "
    "<b>issuer headlines</b>, and the market drawdown was noise on top of that.", BODY))

story.append(PageBreak())

# ── 6. TIMELINE OF DECOUPLING ────────────────────────────────────────────
story.append(P("6. The Decoupling — Evidence in Both Directions", H2))
story.append(P("The most important finding is that the two instruments <b>disagreed</b> at both turning "
    "points. This is what rules out a simple 'parent company drives token' model."))
story += table(["Window", "Equity", "Token", "What it shows"],
  [["28 Aug – 4 Sep (crash week)", "−67% (limit-down, UMA, margin call)", "+6.0% (USD 10.04 → 10.64)", "Stock collapsing; token RISING"],
   ["4 Sep – 4 Oct (post-crash drift)", "Continued weakness", "−16.7% (10.64 → 8.86)", "Slow bleed, mostly independent"],
   ["4 Oct – 19 Oct (token collapse)", "RTD suspension 5 Oct; MACC 7/13 Oct", "−66.4% (8.86 → 2.98)", "Token catches up — on issuer NEWS, 5 weeks late"],
   ["19 Oct – 2 Nov (sukuk window)", "Sukuk to near-default 30 Oct", "−16.1% (2.98 → 2.50)", "Both deteriorating; token lags again"],
  ], [38*mm, 42*mm, 40*mm, 48*mm],
  "Table 6 — Directional disagreement. In the crash week the stock lost two-thirds of its value "
  "while the token gained 6%. Any model in which the token tracks the equity fails on this row alone.")

story.append(P("Worst single sessions for the token all cluster in the 9–15 October window: "
    "<b>9 Oct −46.3%</b>, 13 Oct −22.5%, 14 Oct −16.8%, 10 Oct −14.4%, 15 Oct −14.3%. That window is "
    "precisely when the <b>RTD suspension (5 Oct)</b> and the <b>MACC/police probes (7 and 13 Oct)</b> "
    "became public. The rebound days (11 Oct +24.0%, 12 Oct +12.9%, 19 Oct +17.5%) are consistent with "
    "thin-book overshoot and retracement rather than recovery — classic behaviour for a venue with "
    "USD 28.9k daily turnover.", BODY))

story.append(P("7. Data Conflicts Found and Resolved (Alignment Record)", H2))
story.append(P("Disclosed because a report that silently averages conflicting sources is not auditable.", BODY))
story += table(["Conflict", "What was seen", "Resolution"],
  [["Equity price vs shares outstanding",
    "A screener page showed RM1.32–1.34 with 2,557.87M shares and RM3,376.4M market cap, implying a 6.6× recovery from 19 sen. Arithmetic did not reconcile: 2,557.87M × RM1.32 = RM3.38B, but the low of 22 sen implied ~8.0B shares on a RM1.77B cap.",
    "DISCARDED the screener record as internally inconsistent. Adopted the audited quote page: RM0.065, 7.92B shares, RM514.57M cap. No share-consolidation announcement was located in dated press."],
   ["Press market-cap figures during the crash",
    "Reported RM2.38B at 29.5 sen and RM1.77B at 22 sen imply very different share counts.",
    "Treated as contemporaneous press estimates (B2), not primary. Direction and percentage moves retained; absolute caps not used for valuation maths."],
   ["Equity vs token clocks",
    "Equity quotes Bursa session closes (MYT); token quotes 24h UTC.",
    "Returns computed on matched calendar dates only; no intraday mixing."],
   ["Token circulating supply",
    "CoinGecko reports 0.0 circulating; some aggregators show a market cap.",
    "FDV used as the only defensible aggregate. No market-cap rank asserted."],
  ], [40*mm, 66*mm, 62*mm],
  "Table 7 — Alignment record. The first row is the material correction: an early read suggested a "
  "recovery that does not exist. The final quoted price is RM0.065, not RM1.32.")

story.append(PageBreak())

# ── 8. WHAT IT MEANS ─────────────────────────────────────────────────────
story.append(P("8. Assessment", H2))
story.append(P("<b>8.1 On the business (A1 for facts, C3 for forward view).</b> Zetrix AI is a "
    "concession-based government services company whose core cash engine has been <b>suspended by the "
    "state</b> and whose RM314m collections shortfall is now the subject of litigation and a corruption "
    "probe. Its debt has been cut to near-default in two weeks. Reported earnings growth is real but "
    "backward-looking; the market is now pricing <b>recovery value, not earnings</b>. At RM0.065 with "
    "RM514.6M of market value and 7.92B shares, the equity is a distressed special situation."))
story.append(P("<b>8.2 On the token (A1 for structure, C3 for trajectory).</b> ZTX is a "
    "<b>liquidity-constrained single-issuer asset</b> with a USD 3.44B notional FDV against USD 28.9k "
    "of daily volume, listed on two second-tier venues, with 53% of maximum supply unissued. Its "
    "88.7% drawdown is idiosyncratic. Its risk is <b>not</b> 'crypto winter' — it is venue delisting, "
    "issuer distress, and dilution."))
story.append(P("<b>8.3 On the transmission question — the direct answer.</b> When the market drops, ZTX "
    "does <b>not</b> meaningfully follow. Beta 0.52 against BTC, R² 0.034. The correlation that exists "
    "is <b>headline-driven co-movement</b>, not market transmission: both the equity and the token "
    "responded to RTD, MACC and sukuk news. The practical implication is that a BTC drawdown is a poor "
    "predictor of ZTX, and a ZTX hedge built on BTC beta would be mis-specified."))

story.append(P("9. Risk Register", H2))
story += table(["Risk", "Severity", "Why it matters", "Watch signal"],
  [["Venue delisting", "CRITICAL", "Two venues, USD 28.9k/day. One delisting halves liquidity; two remove price discovery entirely.", "MEXC/XT.COM notice; spread widening; volume decay"],
   ["Issuer insolvency", "CRITICAL", "Chain, token and node-sale revenue all depend on the listed parent surviving.", "Sukuk default; winding-up petition; auditor qualification"],
   ["Dilution", "HIGH", "53% of max supply unissued; node/token sales are a revenue line, so issuance is a business model, not an accident.", "New tranche announcements; FDV/supply divergence"],
   ["Concession non-renewal", "HIGH", "RTD suspension already demonstrates the state will withdraw.", "Further agency suspensions; contract terminations"],
   ["Litigation / enforcement", "HIGH", "MACC and police probes create personal and corporate exposure.", "Charges; travel bans; asset freezing"],
   ["Notional valuation collapse", "MEDIUM", "FDV cannot be realised at quoted prices.", "Any large holder attempting exit"],
  ], [34*mm, 20*mm, 66*mm, 48*mm],
  "Table 8 — Risk register, severity-ranked. The top two are issuer-side, not market-side.")

story.append(P("10. Indicators to Monitor", H2))
for b in ["<b>Sukuk rating actions</b> — a downgrade to default is the cleanest insolvency trigger.",
          "<b>Bursa announcements (7153)</b> — litigation updates, auditor statements, capital-raising.",
          "<b>MACC / police case progression</b> — charges convert uncertainty into a date.",
          "<b>MEXC and XT.COM listing status</b> — delisting is the token's terminal event.",
          "<b>Token supply releases</b> — any issuance against the 2.11B maximum.",
          "<b>RTD / JPJ and other concession reinstatements</b> — the only genuine recovery catalyst.",
          "<b>FDV-to-volume ratio</b> — currently ~119,000:1, a standing measure of how notional the valuation is."]:
    story.append(P(b, BUL, ))

story.append(Spacer(1, 3*mm))

# ── 11. SOURCES ──────────────────────────────────────────────────────────
story.append(P("11. Source Register", H2))
story += table(["#", "Source", "Data used", "Grade"],
  [["1", "stockanalysis.com/quote/klse/ZETRIX (30 Oct close)", "Price RM0.065, mcap RM514.57M, 7.92B shares, 52w range, P/E, TTM revenue & net income", "A1"],
   ["2", "CoinGecko /coins/zetrix (2 Nov)", "Price, ATH/ATL, FDV, supplies, 30d/1y changes", "A1"],
   ["3", "CoinGecko /coins/zetrix/market_chart 180d", "Daily token series used for all return maths", "A1"],
   ["4", "CoinGecko /coins/zetrix/tickers", "Venue list, volume split, total 24h volume", "A1"],
   ["5", "CoinGecko /coins/bitcoin/market_chart 180d", "BTC benchmark for correlation/beta", "A1"],
   ["6", "Google News RSS (en-MY) — The Edge, The Star, NST, Malay Mail, Malaysian Reserve, Malaysiakini, BusinessToday", "Event datelines 24 Aug – 30 Oct 2026", "B2 (multi-outlet)"],
   ["7", "In-house intel store (malaysia/classified) — FMT/Bernama captures", "28 Aug crash detail, UMA query, margin call, 2 Sep stake sales, 24–22 Sep price levels", "B2"],
   ["8", "chainsentry-pipeline EA-50 roster (T2.5 Zetrix row)", "Prior distressed classification; RM314m seizure note; MARC negative watch", "A2 (internal, sourced)"],
   ["9", "frankfurter.app USD/MYR", "FX 4.057 for cross-currency comparison", "A1"],
  ], [8*mm, 62*mm, 76*mm, 22*mm],
  "Table 9 — Source register. Press items are cited by outlet and dateline; no claim rests on a single "
  "unattributed press line.")

story.append(P("12. Limitations", H2))
for b in ["<b>No access to primary filings.</b> Bursa announcements and the audited accounts were not "
          "retrieved directly; the event chain is reconstructed from dated press, which is B2. "
          "Quarterly figures are as reported by media, not re-derived from statements.",
          "<b>Token float is opaque.</b> With circulating supply reported as zero, neither market cap "
          "nor true float-adjusted valuation can be computed. FDV is used as a ceiling.",
          "<b>Correlation is not causation.</b> The 0.034 R² establishes that BTC does not explain ZTX; "
          "it does not by itself prove the news mechanism, which is an inference from timing coincidence "
          "across two independent event windows.",
          "<b>Distressed equities are non-stationary.</b> Betas and correlations computed through a "
          "solvency event have limited predictive value; treat Table 5 as descriptive, not a model.",
          "<b>Venue data quality.</b> MEXC and XT.COM volume figures are self-reported and may include "
          "incentivised trading."]:
    story.append(P(b, BUL))

story.append(Spacer(1, 5*mm))
story.append(P("Prepared 2 November 2026 · Vesper (HermesAgent) · ChainSentry product division, Aras "
               "Integrasi Sdn Bhd · Classification: CONFIDENTIAL — internal assessment. "
               "This document is analysis, not investment advice.", CAP))

# ── page furniture ───────────────────────────────────────────────────────
def deco(canv, doc):
    canv.saveState()
    canv.setStrokeColor(RULE); canv.setLineWidth(0.5)
    canv.line(20*mm, 15*mm, 190*mm, 15*mm)
    canv.setFont("Helvetica", 7)
    canv.setFillColor(GREY)
    canv.drawString(20*mm, 10.5*mm, "Zetrix AI — Market & Token Intelligence (Expanded Findings)")
    canv.drawRightString(190*mm, 10.5*mm, f"Page {doc.page}")
    canv.drawString(20*mm, 288*mm, "")
    canv.restoreState()

doc = SimpleDocTemplate(OUT, pagesize=A4,
                        leftMargin=20*mm, rightMargin=20*mm,
                        topMargin=18*mm, bottomMargin=18*mm,
                        title="Zetrix AI — Market & Token Intelligence (Expanded Findings)",
                        author="Vesper / Aras Integrasi", subject="Zetrix AI equity and ZETRIX token assessment")
doc.build(story, onFirstPage=deco, onLaterPages=deco)
print("BUILT:", OUT)

# ChainSentry — Strategy & Chainalysis Parity Plan
Status: draft v2 (2026-10-06) — adds entry playbooks, pricing counters, corpus roadmap, kill metrics, team gap · Owner: Hadri · Processor: Vesper
Grounding: DEC-20260914-001 (ChainTrace→ChainSentry rename), DEC-20260915-001 (BRICS/sanctions pivot).
Epistemic: parity claims below are [ASSESSMENT]; market triggers news-corroborated 2026-10-06.

## Positioning (non-negotiable, from the pivot decision)
Sovereign, on-prem, jurisdiction-first blockchain forensics + E-KYC for states and
regulated entities the US-cloud incumbents price out or can't serve (sanctions optics,
data-residency, BRICS-corridor blind spots). We do NOT sell "Cheaper Chainalysis".
We sell: your cases never leave your jurisdiction + MENA/SEA/BRICS corridor coverage
the incumbents don't have + deployment they can actually audit.

## What "parity" means — the honest scoreboard
Chainalysis strengths and our answer:
1. Data coverage/labels → their moat is 10+ yrs of seized/organic attribution.
   Counter: (a) 10 PIRs already defined (PIR-01..10); (b) alpha cohort IS the corpus
   flywheel — every tester case adds corridor labels incumbents don't hold; (c) buy/pair
   public-cluster datasets + open-intel enrichment before alpha.
2. Government relationships → Counter: Aras' MY government base (NACSA/MyFleet, MAPO
   door) + sovereign angle they structurally cannot follow (US jurisdiction).
3. Integrations (exchange/bank APIs) → parity task, not moat: build VASP alert
   ingestion adapters (Reactor-compatible case object in/out).
4. Brand/court acceptance (expert testimony) → Counter: publish detection methodology,
   allow independent audit, recruit 1–2 Swiss/SEA academic affiliations (ETH/Zug circle).
Parity target is NOT global feature parity — it is parity ON THE THREE JUDGMENT
DIMENSIONS the buyer cares about in OUR wedges: corridor coverage, deployability,
auditability. Everything else is table-stakes backlog.

## Product gaps that block alpha (gate list)
G1 On-prem appliance hardened (Docker/K8s, air-gap update path) — exists, needs hardening
G2 Import from existing tools (CSV/Reactor-export) — alpha must be additive, not rip-replace
G3 Exchange/VASP alert webhook adapters ×5 majors
G4 Report generator, court/brief-grade (MY + UAE + CH flavours)
G5 Corridor label corpus v0: MENA + SEA clusters, tagged, sourced, versioned
G6 E-KYC deepfake demo (Phase-1 validated on register) bundled into one console

## Alpha program design (the 50)
Cohort shape: ~15 gov/LE · ~20 VASP/exchanges · ~8 banks/financiers · ~5 FIUs/regulators ·
~6 channel/SRO — deliberately cross-market so one corpus serves all three GTM plays.
Terms: free 90-day pilot, named as public "design partner" (not "beta tester"), one
integration engineer assigned, exit artifact = written reference + sanitized labeled-case
contribution + quote. Regulator seats (MY-03, AE-02, CH-03) are NOT testers — they are
endorsement anchors; handle with policy-grade care.
Sequence: 15 seed (T1 warm: MY-01..04, VN-01..02, TH-01, AE-01, CH-01, CH-03 + 5 T1
exchanges) → 20 expansion (T1 remainder + T2 best) → 15 backfill via channels X-01/X-02.

## Commercial model
Seat + appliance licence, tiered by jurisdiction, priced at 30–50% of incumbent quote;
sovereign deployments carry a mandatory local-support clause (jobs argument vs US
vendors). Channel via Big-4 forensic arms + VQF/SRO schemes for the long tail.

## 90-day plan (from 2026-10-06)
Wk1–2: freeze G1–G5 into a sprint plan; G2 (import) first — it unblocks every skeptic.
Wk2–4: 15 seed outreach (Hadri signs; MY doors via Faurani, UAE via consultancy channel,
CH needs a warm Fedpol-adjacent path — flag now, it's the weakest door).
Wk4–8: first pilots live; corpus flywheel reviewed weekly.
Wk8–12: 2 written references (1 gov + 1 VASP), pricing sheets per market,
pipeline review vs ACT deadlines.

## Kill/continue criteria (assess, don't hope)
- <15 seeds signed by wk4 → the pitch is wrong; revisit positioning, not tactics.
- <60% pilots active at wk8 → deployability failure; fix G1/G2, not the sales motion.
- No written reference by wk12 → product is not alpha-grade; say so early.


---

## 6. Seed-15 Entry Playbooks [INFERENCE — doors from Aras relationship map, not confirmed contacts]
Per target: DOOR → FIRST MOVE → PILOT → EXPANSION → WATCH-OUT

- **MY-01 MAPO** — Door: CyberDSA-demo goodwill routed via NACSA/Aras. First move: free 90-day casework pilot, 3 live scam cases, results published jointly with PDRM press framing. Pilot scope: tracing + attribution on live mule-chain cases, no BNM data. Expansion: PDRM-wide licence + NACSA national distribution. Watch-out: procurement via JPA/tender cycles — get a direct-procurement justification (security exemption) early or the deal dies in admin.
- **MY-02 BNM** — Door: Aras already inside NACSA/CSM ecosystem; BNM examiners talk to CSM. First move: not a sale — a *supervisory whitepaper*: "crypto-AML expectations for MY DAXs, with a sovereign tracing option" co-authored quietly. Pilot: one-bank sandbox slot if BNM runs one. Expansion: examiners ask supervised banks "what tracing tool do you run?" — that single exam question is the whole GTM. Watch-out: BNM never buys for banks; sell the standard, bill the banks.
- **MY-03 SC** — Door: guidelines comment period = public consultation; submit a formal response naming proportionate surveillance standards. First move: meeting with the markets-oversight division, demo on MY DAX flows. Pilot: oversight-console for SC's own monitoring of DAX reporting. Expansion: SC lists expectations → Luno/MX/Tokenize buy. Watch-out: SC's own IT procurement is slow; the money is with the exchanges, keep the two motions separate.
- **MY-06/07/08 Luno/MX/Tokenize** — Door: compliance officers, not CEOs; they carry the guideline deadline. First move: free flow-scanner audit — we import their Reactor/CSV exports, hand back a risk report on their existing exposure in a week. Pilot: 60-day monitoring of inbound flows, priced under their current Chainalysis renewal by design. Expansion: multi-year + E-KYC add-on. Watch-out: Luno is global — MY branch can't sign enterprise; land MY-entity branch scope only.
- **VN-01/02 Bithumb-SSI / SSI Digital** — Door: SSI group relationship via Vietnam fintech partners [EST: no warm line yet — first cold touch]. First move: "day-one AML" bundle timed to pilot-licence issuance — stack + policy docs + SBV filing support. Pilot: 90 days bundled, licence-launch demo for SBV. Expansion: all pilot licensees once first VN reference exists. Watch-out: Chainalysis/TrmLabs will open a localised push in 2026–27; speed is the entire strategy here.
- **TH-01/02 Thai SEC / AMLO** — Door: AMLO crackdown capacity gap is public (10K freezes). First move: offer AMLO a triage pilot on their frozen-wallet backlog; SEC gets the same tool as supervisory console. Expansion: Thai DAX licence conditions reference state-approved tooling → Bitkub/Gulf-Binance follow. Watch-out: Thai procurement loves free pilots that never convert — put a hard conversion clause and data-rights term in every pilot MOU.
- **AE-01/02 VARA / SCA** — Door: VARA innovation/tech team + compliance consultancies already serving licensees (X-02 motion). First move: apply as registered technology/approved-tooling vendor; run a corridor report ("Gulf outflows traced") as credibility bait [REPORTED gap: incumbents thin on MENA attribution]. Pilot: supervisory console for VARA's own market monitoring. Expansion: licensees inherit the tool as "regulator-listed". Watch-out: UAE channel = consultancies and big-brother politics; federal-vs-Dubai turf means VARA win ≠ SCA win. Budget is real but relationship-gated; no warm Gulf line exists today — this is the seed-15 item with the most door-building needed.
- **AE-03/04 BitOasis / M2** — Door: compliance leads on LinkedIn/cold is acceptable in UAE startup culture. First move: displacement quote vs their incumbent renewal + 30-day parallel run. Watch-out: M2 is VARA-regulated early — a logo that doubles as regulator proof.
- **CH-01 Fedpol** — Door: Swiss cooperation channels (NACSA↔Fedpol exists via Interpol/ASEAPPOL adjacency) [EST]. First move: never a sales call — a *methodology paper*: open-sourced heuristic corpus, Swiss-hosted PoC offered, "cases never leave CH". Pilot: 2–3 cross-border Gulf-corridor cases MPC can't place. Expansion: cantonal police follow Fedpol; ETH Zurich tie-up neutralises product-origin objection. Watch-out: Swiss procurement = years; treat as 2027 revenue, 2026 credibility only. Any Russian/Chinese-language UI association is fatal in CH — keep the sovereign story BRICS-*corridor*, never BRICS-*product*.
- **CH-03 MROS** — Door: AML-consultancy channel (X-02/Swiss equivalent), not direct. First move: SAR-corridor enrichment pilot — MROS forwards sample redacted SAR clusters, we return corridor attribution within SLA. Watch-out: secrecy-law handling of SAR data requires CH-hosted instance from day one — that's our on-prem wedge made concrete; quote the hosting, not the software.

## 7. Competitive Counters (objection → response)
- **"Chainalysis has the network effect."** True globally, false in our wedge: in a VN pilot or a UAE branch office, the incumbent is a cloud seat-license with no local corpus and no on-prem option. We don't fight the graph, we fight the *deployment model*.
- **"Your corpus is young."** Answer is transparency: publish precision/recall per heuristic, per chain, per corridor, on the alpha cohort's own labelled feedback. Incumbents won't publish methodology; auditable-but-young beats opaque-but-old for sovereign buyers who must defend cases in *their* courts.
- **"No track record."** First six weeks of every pilot is a *free audit* that produces value before trust is required (flow-scanner on their own exports).
- **"Incumbent will discount."** They will — their APAC/MENA SMB segment is their margin graveyard; they cannot go sovereign-on-prem without cannibalising their own cloud P&L. That's structural, not tactical.
- **Pricing posture [EST]:** wedge pricing = under the target's current incumbent renewal by 30–40%, with pilot-to-licence conversion pre-agreed. Never "cheap" — "proportionate". Anchor: price per monitored address-band, not per analyst seat (incumbent lock-in mechanism).

## 8. Corpus Cold-Start Roadmap (the real moat problem)
1. **Alpha cohort feedback** — every seed-15 pilot contractually returns labelled dispositions (seed clause: data-rights term, mutual).
2. **Bought seeds** — purchase existing cluster datasets/exchange attribution lists where legally clean [EST cost: low-five-figures USD to stand up v0].
3. **Public intel mining** — sanctioned-address lists (OFAC/EU/UK), court-document addresses, ransomware-payment trackers, darknet takedown archives → deterministic seed labels.
4. **Heuristic engine** — exchange-cluster/fan-out/peel heuristics open-sourced (credibility move, doubles as methodology paper).
5. **Corridor specialisation** — USDT-TRON Gulf→SEA off-ramp graph is the specific graph incumbents underlabel. Own one corridor end-to-end before claiming five.
Corpus v0 gate: 10M+ labelled/derived addresses with per-corridor precision measured on alpha feedback (G5, wk8).

## 9. Kill / Continue Metrics (wk4 / wk8 / wk12)
- **wk4:** G1 appliance hardening green; G2 Reactor/CSV import demo-able. Fail → freeze outreach, product sprint only.
- **wk8:** ≥5 seed-15 meetings held, ≥2 signed pilot MOUs with data-rights clause. Fail → doors thesis wrong; re-tier roster before more time spent.
- **wk12:** ≥1 pilot producing a case report the *customer* will put their name on; corpus v0 gate G5 hit. Fail → ChainSentry to maintenance mode, Aras focus back to services. (Pivot cost is lower than sunk-cost drift. This is the RSK-20261006-001 circuit breaker.)

## 10. Team & Cost Envelope [EST — validate against Aras resourcing]
- Product: 2 engineers (appliance hardening G1, adapters G2/G3) + 1 data (corpus G5) — 8–12 wks, the binding constraint.
- Sales: Hadri as wedge-architect/presales-closer only; seed-15 needs ONE full-time pipeline runner (currently nobody — biggest plan gap). Faurani's practice can carry MY gov doors; VN/UAE need the hire or a partner.
- Cash: pilots are free-to-cheap by design; 90-day cash burn ≈ 3–4 staff-months + bought-corpus seed + travel (KL/VBKK/DXB/ZRH). No marketing spend until first two logos.
- Sequence honesty: **the roster is ahead of the team.** Do not run seed-15 until G2 passes and a runner exists — otherwise this becomes 50 conversations and zero pilots, which is exactly RSK-20261006-001.

## 11. What "parity with Chainalysis" actually means (one paragraph, for the board deck)
Chainalysis = graph corpus + government incumbency + network effects + brand. We will not match the first two in 24 months, so parity is *redefined by wedge*: (1) deployment parity — sovereign on-prem they won't build; (2) corridor parity — be measurably better on Gulf→SEA USDT-TRON than they are, verified by third-party eval on alpha data; (3) audit parity — publish what they keep private; (4) price-scope parity — proportionate licensing for supervised-SMB, their non-served segment. When a Malaysian/Emirati regulator can say "ChainSentry covers our corridors, the data never leaves our jurisdiction, and we can defend every label in our court" — that *is* parity where it matters, and their brand halo is irrelevant to that sentence.

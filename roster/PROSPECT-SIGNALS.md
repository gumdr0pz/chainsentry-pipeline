# ChainSentry Malaysia — Hiring-Signal Intelligence (layer 2)

Mined 2026-10-10 from live job-board traffic (LinkedIn public postings API, KL-filtered, 53 unique current postings, JD bodies pulled individually). This layer is NOT directory data — it shows WHO IS BUILDING A FINANCIAL-CRIME FUNCTION RIGHT NOW, WHICH STACK THEY NAME, and WHEN THE DOOR OPENS. Hiring for these roles predicts tool purchases 6–12 months out. Each posting = dated, click-verified.

## A. The headline: KL is becoming a regional crypto-AML hiring hub — and the named stack is the incumbents we displace

### Bybit Kuala Lumpur hub — SIX AML/risk postings within 18 days (22-Sep → 09-Oct-2026)
- Principal/Lead Crypto Capital Risk Engineer (22-Sep) · Sr AML Specialist Transaction Monitoring (1-Oct) · Sr AML Specialist KYB (7-Oct) · Lead AML Specialist (9-Oct) · Sr AML Specialist Investigations (9-Oct) · Sr AML Specialist Name Screening & Travel Rule (9-Oct)
- JDs NAME THEIR STACK: "utilize blockchain analysis tools and transaction monitoring systems such as **Chainalysis, Elliptic, TRM Labs**... **CipherTrace**" (jobPosting 4466869011, 4470754898) → incumbent relationship or aspirational skillset; either way = displacement target with named competitors.
- Travel Rule specialist role (4476267709): sanctions/PEP/adverse-media + "resolve failed transmissions, liaise with counterparty VASPs" = Travel Rule ops pain = exactly our corridor-coverage wedge.
- **Buyer insight: Bybit's roster row is AE-09 (UAE entity). WRONG GEO. The AML buying center sits in Kuala Lumpur.** Roster corrected: MY buying center flag + T1 candidate (exchange, MY-adjacent).
- Pitch angle: 12-months-out they need monitoring tuned for the corridors their KL desk investigates (SEA mule chains, Gulf off-ramps) — the thing Chainalysis prices as an add-on, we ship as core, on-prem option for their regulator talks.

### TNG Digital — **Head of Financial Crime Compliance (FCC)** — posted 23-Sep-2026 (jobPosting 4470672804)
- Department-head level, not staff: "strategic direction AML/CFT/TFS & CPF", "primary liaison with regulators, **financial intelligence units**", "supervise transaction monitoring systems" — JD names NO incumbent tool = stack undecided at this seat.
- **This is the single highest-value timing signal in Malaysia right now:** whoever takes this seat buys the FCC stack for TNG's next cycle. A department head arriving without a mandated tool = 6–12 month purchase window OPEN until the hire lands and settles.
- Corroborates T1: the TNG/PayNet fraud-alert pilot (BNM orbit, Oct-2026) is being staffed at head level = the mandate is real and funded.
- Move: ChainSentry brief aimed at this seat (and the interim): on-prem + FIU-liaison-grade reporting + MY corridor corpus. If our AML/CFT hire (ACT-20261008-002) lands first, ex-incumbent-side candidates who lose to TNG's process are also our hire's feeder pool.

### First Digital (FDUSD — the MYR-stablecoin-adjacent issuer, KL desk) — Compliance Operations Analyst (15-Sep-2026)
- Compliance *operations* hire = building the ops layer = tooling follows headcount. Watch-list prospect; no stack named.

### StraitsX → "Monee" (KL stablecoin/payments cluster, ShopeePay nexus) — AML Agent (1-Oct) + OTC Sales Manager (9-Oct)
- Two-track hire (compliance + institutional OTC) = institutional flow scaling. Prospect-discovery entry; verify entity naming before outreach (brand confusion = our diligence gap).

### Doit (PJ; doit Global) — Compliance Officer (8-Oct)
- JD: reports directly to CEO, admin line to board-level — first-cohort compliance build = greenfield, tiny fish, channel-partner bait only.

### Razer (Shah Alam) — Fraud & Transaction Monitoring Specialist (9-Oct)
- Payments fraud monitoring at a consumer-payments giant; adjacent prospect tier (no chain focus in JD). Track.

## B. Where the banks' KL back offices signal: UOB (5 AML postings Sep–Oct), OCBC (5), MUFG (2), Citi (1), Cigna (1)
- Persistent AML hiring at SEA banks' KL hubs = regional AFC capacity build-out; their group stacks (Actimize/NICE class) are locked, but KL hubs staff the *investigations layer* our case-tooling serves. Tier-3/channel intel, not T1 pipeline. Deloitte KL Forensic & FinCrime hiring 4 roles (Sep–Oct) = **channel signal**: the consultancy staffing the local AML remediation market = our Path-4 partners buying subsurface tooling for client work.

## C. What this layer changes in the plan (committed with this file)
1. **AE-09 Bybit: buying center = KL, not Dubai.** Outreach geo/localization change; stack intel = displace named incumbents (Chainalysis/Elliptic/TRM/CipherTrace appear verbatim in their own JD).
2. **TNG re-timed: NOW, not "their cycle."** Head-of-FCC window open ≤6 months. First non-JSJK proactive door we can knock with a dated reason ("congratulations on standing up FCC" beats cold pitch).
3. **New prospect cluster (roster additions warranted): Bybit MY desk (T1), First Digital (T2), StraitsX/Monee (T3-verify), Razer (T3).**
4. **Channel:** Deloitte KL FinCrime = Path-4 first-approach candidate with evidence they staff delivery.
5. Hiring-signal sweep is now a **recurring Friday loop** (endpoint works from this host; ~10 calls, full-market KL snapshot). Diff = campaign timing.

## Method (reproducible)
LinkedIn jobs-guest public API: `linkedin.com/jobs-guest/jobs/api/seeMoreJobPostings/search?keywords=<K>&location=Malaysia` (curl, Mozilla UA) → card parse → per-posting JD body via `/jobs/api/jobPosting/<id>` → tool-name scan (Chainalysis|Elliptic|TRM|Actimize|NICE|Featurespace|ComplyAdvantage|World-Check|LexisNexis|Tookitaki|…30-term list) + reporting-line extract. Raw: /home/mtadmin/.hermes/workspace/li_jobs_my.json · JD bodies /tmp/jd_*.html · parsed /tmp/jd_analysis.json.
NOT FOUND / tried: JobStreet & hcareers search endpoints (blocked/404 from host); Luno/Maybank/CelcomDigi own ATS pages not yet swept (next loop; their postings often sit behind Greenhouse/Workday subdomains).

# COMPETITION-01 — TRM Labs: Know-the-Competitor Plan (End-to-End)

**Status:** DRAFT v1 (2026-10-16) · Owner: Hadri (approval) · Operator: Vesper (execution)
**Purpose:** ChainSentry displaces TRM-class incumbents (their own JDs name Chainalysis/Elliptic/TRM/CipherTrace; TNG's FCC seat decides a stack within 6 months). Knowing TRM end-to-end = the difference between pitching features and pitching THEIR gap. This plan operationalizes that knowledge: product teardown → technical layer → commercial layer → GTM layer → deliverables → continuous watch.
**Standing rule:** NOT FOUND beats guess. Auth-gated surfaces (MyTRM portal, docs API-reference, member Slack/community internals) are marked as boundary conditions, never guessed.

---

## PHASE 0 — Objectives & the four questions (everything serves these)
1. **What does TRM actually ship** — per-product feature truth (not brochure truth)?
2. **Where are their structural gaps** — geographies, currencies, deployment models, price points, segments they underserve?
3. **How do they earn trust** — certifications, communities, regulator relationships, services — and what can ChainSentry replicate cheaply?
4. **What is their roadmap telegraphing** — hiring signals, launch cadence, partner moves?

**Deliverable set (end-to-end):** (D1) product inventory + feature matrix · (D2) battle card vs ChainSentry M1–M5 · (D3) gap/opportunity memo feeding Paths 1–2 · (D4) trust-replication playbook · (D5) roadmap-inference memo from hiring · (D6) monitoring loop spec.

## PHASE 1 — Product teardown ✅ EXECUTED 2026-10-16 (evidence: live crawl, this session)
All surfaces fetched from www.trmlabs.com (Next.js site; cloudflare edge) + status/support/docs subdomains. Boundary hit: docs API-reference is auth-gated (login) — endpoint truth beyond public OpenAPI hints NOT accessed, no credentials attempted.

**Product inventory (verified at source 16-Oct):**
| Product | What it is (site's own words, condensed) | ChainSentry analogue |
|---|---|---|
| **Ardence** | "The AI investigation platform" — all-source investigations; NEW flagship (launch PR featured) | M3 cockpit (ours: younger, narrower) |
| **Forensics** | Core tracing: 65+ blockchains, 1.9B digital assets; **"glass box" attribution** (source + confidence score per attribution — claimed unique); Signatures® (peeling chains, layering, change-of-custody detection); cross-chain tracing; multi-route pathfinding; victim-reports DB ("largest scam/fraud victim reports db"); BTC transaction fingerprinting; case management; graph customization/export; **Seed Analysis** (associated wallets from seed phrases); Co-Case Agent (AI assistant, "human-led, court-defensible") | M3 + M2 (signatures ≈ our typology engine) |
| **BLOCKINT API** | <500 ms latency; **184+ chains incl. native EVM tokens**; address behavior, risk exposure, wallet flows, tx history; verticals named: Defense, Regulators/supervision, Tax authorities | Our G2/API layer |
| **TRM Triage** | Search crypto identifiers for rapid evidence | Piece of M1/M3 |
| **TRM Detect** | Continuous address monitoring + instant email alerts; "revive cold investigations" | M2 (alerting leg) |
| **Bulk Data** | **3.1B+ addresses attributed**; address/entity risk-exposure analytics for mission-critical datasets | Corpus (G5) — their number is the bar |
| **Beacon Network** | Real-time crypto-crime RESPONSE network: deposit/withdrawal flagging, member exchanges act before withdrawals. Founding members quoted: **Binance (Noah Perlman, CCO), Coinbase (Valerie-Leila Jaber, Global Head AML), Kraken (CJ Rinaldi, CCO), Ripple (Andrew Rosenberg, Head FCC)** | No analogue — a NETWORK moat, not a feature |
| **Deconfliction (TRM Deconflict)** | FREE for verified LE: wallet-overlap deconfliction across agencies; secure coordination w/o case-file exposure | No analogue — community moat, zero-cost hook |
| **Chainabuse** | Community scam-reporting platform (external) | No analogue — crowd intelligence funnel |
| **Leo Labs** | LE community: APAC/LATAM/EMEA working groups, training (DPRK tracing, AI-in-crime), named speakers incl. ex-FBI/K-NPA/BFP/INTERPOL | Our PDRM briefing ≈ embryonic version of this |
| **Services** | Embedded Investigator (FT), On-Demand (hours), Ask-the-Investigator (office hours) — staffed by ex-agency investigators | Hire-centric services lateral |
| **Training / Academy** | TRM Academy resources; compliance training | JWT: our T0 ramp is internal; theirs is a funnel |
| **TRM MCP** | AI-agent integration: 12+ composable skills, full TM alert lifecycle (triage→context→exposure→node analysis→dismiss/escalate with WRITTEN justification→audit trail marked MCP-originated); 180+ data points; targets Claude Code/Gemini/OpenAI Codex/custom agents | **Wake-up call:** agent-native compliance ops is shipping NOW |

**Trust layer (replication targets):** SOC 2 Type II · ISO 27001 · ISO 27701 · UK CyberEssentials+ · GDPR · Drata Trust Center (public trust portal) · annual third-party pen tests · status page · NPS 80+ claimed · research arm (Crypto Crime Report, Capacity Gap, AI-in-Crime Adoption Index).
**Statistics to beat in our pitches (site-claimed):** 65+/184+ chains (context-dependent), 1.9B assets, 3.1B addresses, <500 ms, NPS 80+, "only glass-box attribution."

## PHASE 2 — Feature-vs-gap analysis (build: D1/D2) — PLAN
- **Matrix build:** every Phase-1 product row × ChainSentry M1–M5 × (fiat leg / crypto leg). Field: parity / partial / none / *structural gap*.
- **Known structural wedges to test (hypotheses, Phase 4 validates):** (a) fiat-rail depth (TRM is crypto-native; MY banks/e-money need fiat mule-chain AML in the SAME case tool) · (b) sovereign/on-prem deployment (TRM = cloud SaaS; MY/GCC data-residency mandates) · (c) corridor attribution Gulf⇄SEA corpus depth · (d) MY-language/regulator-format localization (BM reporting, BNM/FIED formats) · (e) price accessibility for Tier-2/3 FIs and LE units (TRM priced enterprise).
- **Battle card (D2):** one pager per Path-1/2 door — their claim, our counter, the question to plant in the buyer's head ("who shows YOU the attribution source and confidence?" — if glass-box is their crown, our parallel-reconstruction workflow must match it or dodge it).

## PHASE 3 — Technical/OSINT layer (build: D1 footnotes) — PLAN
- **Public API surface:** docs.trmlabs.com public guides (Chainabuse API, Sanctions intro) mined for data-model vocabulary; api-reference gated — request trial access decision belongs to Hadri (boundary: no credential work without directive).
- **status.trmlabs.com telemetry:** subscribe/feed-watch → incident patterns reveal infra posture (regions, dependencies) feeding the sovereign-deployment pitch.
- **Careers mining (D5):** TRM jobs postings (greenhouse/Lever boards) monthly diff — roles = roadmap telegraph (new chains, fiat features, regions). Feeds hiring-signal lane (evidence/ pattern exists).
- **Changelog watch:** tech blog + product blog + press center monthly diff.

## PHASE 4 — Commercial layer (build: D3/D4) — PLAN
- **Packaging/pricing:** public pricing absent (sales-led) — collect from: purchasing portals/quotes, procurement disclosures, design-partner anecdotes, secondhand ranges; never present as fact without source grade.
- **Partnership map:** Beacon membership roster (quoted members + announcements), Big-4/consultancy alliances, exchange data-sharing deals → who's locked (avoid), who's reachable (pitch).
- **Beacon imitation assessment (D4):** a MY/GCC "settlement-risk network" (banks+e-wallets+DAXs flag mule wallets pre-withdrawal) is the highest-leverage community moat ChainSentry could seed with NACSA/PayNet orbit doors — costed proposal memo.
- **Free-tier play (D4):** Deconflict is FREE-for-LE — their funnel hook. Our equivalent: free public-data casework triage for MY LE units (Path 1 wedge already half-built; formalize as product tier decision).

## PHASE 5 — GTM analysis (feeds Paths 1–2) — PLAN
- Vertical-mapping: their 12 mission verticals vs our two-market canon — which verticals they WIN (enterprise sanctions/fraud at global exchanges) vs where MY/GCC demand diverges (sovereign LE casework, national supervision consoles, fiat-first banks).
- Leo Labs imitation lite: quarterly MY working group (invite-only, PDRM/BNM/SC/DAX compliance desks) — community-before-commerce, mirrors their own playbook at corridor scale.
- Services tiering: our hire's embed offer (JD v4) already mirrors "Embedded Investigator Support" — price-position beneath TRM with corridor specificity.

## PHASE 6 — Synthesis & records (wk4 of plan)
- D1–D6 assembled into `competition/` set; battle card lands in sales kit; gap memo → DEC/INT records (CognitiveOS PROPOSE → MERGE on approval).
- Readout to Hadri: 30-min brief, one-page verdict + D2/D3 attached.

## PHASE 7 — Continuous watch (recurring, monthly)
| Watch | Source | Cadence | Output |
|---|---|---|---|
| Product/release | trmlabs.com press + product blogs + status | monthly diff | roadmap-inference memo delta |
| Hiring | TRM job boards | monthly diff | D5 update |
| Network growth | Beacon member announcements | event-driven | partnership-map delta |
| Their-vs-us stats | public numbers (chains/assets) | quarterly | battle-card refresh |

Loop parked as monitor-spec ONLY (no cron monitor per standing directive); fires on Friday sweeps when instructed.

## GOVERNANCE
- **Owner decisions needed:** ① authorize trial-account request for gated docs/API (yes/no); ② commission Beacon-imitation costing (yes/no); ③ battle-card audience (sales team only / + Hadri brief); ④ Phases 2–4 in-house or delegate to a subagent sweep batch.
- **Kill/scope rules:** no credential access, no member-portal scraping, no outreach to TRM staff posing as buyers (passive public OSINT only); every site-claimed stat carries [SITE_ASSERTION] grade until independently sourced.
- **Verification state:** Phase 1 = live-crawl evidence this session (files cached /tmp/trm_pages, /tmp/trm_inventory.json — to be re-pinned into chainsentry-pipeline/competition/evidence on next commit); Phases 2–7 planned. Hiring/statistics numbers are site-claimed; NPS/stats = [SITE_ASSERTION · single-source].

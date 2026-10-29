# Blockchain Developer (Junior / Middle) — Forensics & Data Platform

**Position ID:** CS-DEV-001
**Version:** v1 — new position
**Owner:** Hadri (COO, approver) · **Prepared:** Vesper · **Band status:** INDICATIVE — owner confirmation before posting
**Company:** Aras Integrasi Sdn Bhd — ChainSentry Product Division
**Product line:** ChainSentry (sovereign blockchain forensics + E-KYC) and the chain: family — chain:HARVEST wallet intelligence
**Reports to:** Solutions Architect / Product Lead, ChainSentry — engineering mentoring from the senior engineering bench
**Team context:** Small product-engineering pod alongside the intelligence/data pipeline that feeds it
**Grade:** Two bands hire against this single posting — Junior (0–2 years) and Middle (2–4 years)
**Location:** Kuala Lumpur, Malaysia (hybrid)
**Type:** Full-time, permanent; three-month probation with structured objectives
**Remuneration:** Band aligned to the Malaysian engineering market by level (INDICATIVE pending COO confirmation before posting); medical coverage; hardware and learning budget

---

## 1. About Aras Integrasi and ChainSentry

Aras Integrasi Sdn Bhd is a Malaysian technology and security integrator with an established government and regulated-industry client base, including national security-agency deployments. **ChainSentry** is the company's sovereign blockchain-forensics and E-KYC product line: jurisdiction-first blockchain intelligence for governments, financial-intelligence units, banks and licensed virtual-asset service providers that US-cloud vendors price out or cannot serve — on-premises, auditable, and built for Gulf–Southeast Asia–BRICS corridors.

The stack you would join is real, deployed, and unusual for its size:

- **ChainSentry forensics app** — Next.js 16 / TypeScript with a graph-exploration core (Cytoscape with fCoSe/Dagre layouts), React Query data layer, authenticated role-based access (NextAuth), and an in-app sanctions-import pipeline.
- **A TypeScript MCP server layer** exposing ChainSentry capabilities as tools (single- and multi-source variants) so agentic systems can drive forensics workflows.
- **chain:HARVEST** — a Python wallet-intelligence system: crawler fleet across dark-web forums, ransomware-leak sites, Telegram channels, paste sites and clearweb crypto communities; checksum-validating ingestion (Base58Check, Bech32/Bech32m per chain); enrichment engines (contract vs EOA classification via live RPC, token-symbol resolution, explorer backfills); and an OFAC compliance engine (SDN parsing, wallet matching, risk scoring, reporting) — every address checksum-validated before entering the database, no exceptions.
- **PostgreSQL** storage, Docker-based deploys, Linux production hosts.

Two things make this seat scarce: you will work across a forensics **product** used by investigators, and the **data machinery** that feeds it — most developers see one or the other. And the work is sovereign-stack: where a foreign vendor ships a black box, here you will build and be able to explain every layer.

## 2. About the Role

You will build the ingestion, validation, enrichment and exploration machinery that turns raw multi-chain data into evidence-grade intelligence. Middle hires will own subsystems end to end within the first quarter. Junior hires will pair with the senior bench, own first features in weeks, and be taught the codecs, the pipelines and the investigative mindset from the inside. In both cases: your code runs in production at customer sites, and the habit this team is built on is that **every datum entering the corpus carries provenance**.

## 3. Key Responsibilities

### 3.1 On-chain data engineering
- Build and maintain ingestion services that acquire, parse, normalise and index on-chain data across multiple networks (Bitcoin-family, Ethereum/EVM, TRON, Solana), from raw RPC through to storage.
- Implement and extend address-codec validation per chain — Base58Check, Bech32/Bech32m, EIP-55 checksums — treating validation as a gate, not a suggestion.
- Work with the crawler fleet's output: idempotent upserts, deduplication across sources, schema evolution without losing provenance columns.

### 3.2 Enrichment and intelligence pipelines
- Extend the enrichment engines: contract-vs-EOA classification via `eth_getCode`, token-metadata resolution, explorer reconciliation, sanctions-list joins.
- Build new collection veins as coverage expands (including privacy-coin transparent-address handling and cross-chain bridge event mapping).
- Keep false-positive rates measurable: every heuristic gets a precision story, and you will instrument it.

### 3.3 Forensics product features
- Ship investigator-facing features in the Next.js/TypeScript app: cluster-graph exploration, trace timelines, case-pack export, watchlist views.
- Own the graph layer pragmatically — layout performance on large clusters, sensible edge semantics, clean interaction for non-technical examiners.

### 3.4 Sanctions and compliance engineering
- Harden the sanctions-import path: OFAC SDN (XML/JSON/CSV), EU/UK/UN list variants, deterministic address extraction, versioned and dated imports.
- Tune matching behaviour with the AML/CFT SME: exact vs fuzzy matching thresholds, coin-type validation, scoring weights — with documented, reversible changes.

### 3.5 Surfaces and integrations
- Maintain and extend the MCP tool layer so agentic clients can consume ChainSentry capabilities safely (authentication, scoping, tool contracts).
- Build and maintain internal APIs consumed by the app, the pipelines, and partner integrations.

### 3.6 Quality, security and operations
- Practise the team's discipline: checksum-validated ingestion, secret-free commits, dependency review, migration discipline on PostgreSQL, containerised deploys to Linux hosts.
- Take part in deployment and incident triage for owned systems — you ship it, you keep it alive.

## 4. Success in the First Twelve Months

| Horizon | Outcome — acceptance-test wording |
|---|---|
| Day 30 | At least one shipped ingestion/validation change in production with tests; can walk through the codec stack (Base58Check vs Bech32m vs EIP-55) unaided; first PR merged into the crawler or app codebase |
| Day 90 | Owns one ingestion vein end to end (source, validation, storage, monitoring); one enrichment heuristic instrumented with a measurable precision figure; onboarding doc for that vein exists |
| Month 6 | Delivers a forensics app feature through to production (Middle) or a significant component of one (Junior); sanctions-import path handles at least two list variants deterministically; participates in deploy rotations |
| Month 12 | Recognisable owner of a subsystem the AML/CFT SME trusts for casework evidence; MCP/tooling contributions shipped; zero data-provenance regressions attributable to owned code; able to brief a non-technical reviewer on the corpus's data journey |

## 5. About You

**Required (both bands)**
- JavaScript/TypeScript and Python are your working languages; SQL (PostgreSQL) is second nature.
- Concrete grasp of blockchain fundamentals: transactions, UTXO vs account models, addresses vs keys, confirmations, and why address encodings differ per chain.
- Git discipline you do not have to be reminded about; comfort in Linux environments; willingness to carry deploys.
- Bias to verification: you would rather measure than assert — checksums, tests, logs.

**Additional for Middle (2–4 years)**
- Production experience in at least one of: data-pipeline/backhaul engineering, Web3/on-chain services, or fintech backend systems.
- Demonstrable asynchronous-worker and queue patterns; schema-evolution experience on live datasets.
- Familiarity with at least one major chain's tooling ecosystem (ethers/viem, bitcoinlib, explorer APIs).

**Additional for Junior (0–2 years)**
- A portfolio that proves hands-on work: shipped projects, freelance builds, or substantial open-source/contribution history touching blockchains, scrapers, or data tooling.
- The trajectory matters more than the years: evidence you learn fast and finish things.

**Nice to have**
- Rust or Go alongside the core stack.
- Front-end graph experience (Cytoscape, D3, xyflow) or real MCP/tool-API design.
- Privacy-coin curiosity (Zcash address model, transparent vs shielded flows) — a deliberate product wedge; you would help build its first vein.
- Docker production operations; conversational Mandarin for regional vendor coordination.

## 6. What We Offer

- Production ownership uncommon at this level: your services run in sovereign deployments where a foreign vendor would be a black box.
- Dual craft development: data engineering and forensics product work in one seat.
- Direct access to the product lead and the AML/CFT SME; no layers between your code and the investigator who uses it.
- Hardware and learning budget; funded attendance at regional security/blockchain community events.
- A stated kill/continue culture — measured results and honest bad news beat managed optimism.

## 7. Engagement Terms

Full-time, permanent; KL hybrid; band **INDICATIVE pending COO confirmation before any posting** (junior and middle bands distinguished by level); probation three months with structured objectives; NDA applies — portions of the work touch law-enforcement-adjacent casework and customer compliance data.

## 8. Application Process

Submit CV or portfolio plus a short note on a piece of data tooling you built and what broke first. Shortlisted candidates complete a practical exercise: validate, ingest and enrich a small raw address dataset (codec edge cases included) and walk through your choices in a technical conversation. Applications to **[careers contact — confirm before posting]**.

---

## Appendix — Stack Anchors, Comparators and Verification Ledger
**REMOVE BEFORE POSTING**

**Stack anchors ([FACT] — repo reads, 2026-10-29):** chainblock `package.json` (Next.js 16.2.6, TypeScript, Cytoscape + dagre/fcose, @xyflow/react, React Query, NextAuth, MCP servers, sanctions-import scripts); chainharvest repository (crawler fleet, checksum-gated ingestion, enrichment engines, OFAC compliance engine, PostgreSQL layer, v3.3.0 README with 88,481 verified wallets / 99.94% checksum pass rate).

**Comparator JDs (genre grammar; never content):**
- Binance — "Blockchain Engineer – Binance Wallet" (Greenhouse id 5002619101), pulled 2026-10-29: on-chain data acquisition/parsing/indexing verb stack; full-lifecycle ownership framing; "mainstream ecosystems" requirements line adapted to multi-chain codec requirement.
- Coinbase / Ripple board scans, 2026-10-29 (228/108 jobs): senior-software-engineer titling conventions noted; Ripple full-stack London/Dublin postings — "Manager/SE, Software Engineering" grammar. No junior/middle crypto-native postings pulled that beat the genre basics; local MY market norms govern banding.

**Verification ledger:**
- [FACT] Product/stack/company claims — repositories read 2026-10-29 (chainblock package.json, chainharvest README/CHANGELOG/OFAC docs).
- [INDICATIVE] Bands and benefits — pending COO confirmation before posting.
- [UNKNOWN] Careers contact — to be inserted before posting.
- [UNKNOWN] Whether the E-KYC layer (UKM MyVAM pipeline) reaches integration maturity within this hire's first year — roadmap per DEC-20260915-001; deliberately not promised in the body copy.

*— End of document —*

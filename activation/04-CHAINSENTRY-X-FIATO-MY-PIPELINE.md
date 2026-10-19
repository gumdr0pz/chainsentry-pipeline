# 04 — Collaboration Pipeline: ChainSentry × Fiato Malaysia

**Status:** DRAFT v2 (2026-10-16) · Owner: Hadri (approval) · Operator: Vesper (execution)
**Scope correction (Hadri, 16-Oct):** the collaboration is bilaterally scoped — **ChainSentry for Fiato Malaysia**. ChainSentry plugs into Fiato's crypto-to-MYR settlement service as its compliance & forensics engine. Group repositioning ("financial & blockchain platform" broadly) is parked; v1 of this file is superseded.
**Basis:** DEC-20260915-001 · ACT-20261008-002 (AML/CFT hire, due 22 Oct) · JD v4 (Fiato MY × ChainSentry dual mandate) · 01-ACTIVATION-PATHS v1 (unchanged) · 02-MASTER-PLAN (gates stand)

---

## 1. The collaboration in one paragraph

Fiato Malaysia settles crypto payments into Ringgit in real time. Every settlement it processes is a compliance event: the inbound crypto leg must be screened, monitored and provable to BNM; the fiat leg must survive partner-bank due diligence; the company itself must become exam-ready under the Malaysian regime. **ChainSentry becomes the engine under all three** — screening, monitoring, and evidence — deployed as Fiato's compliance infrastructure. Fiato is simultaneously ChainSentry's first production deployment, its founding payments-sector reference, and its live case study. One collaboration, both products advanced.

## 2. Why bilateral and why now

- **Fiato's binding constraint is trust** (JD v4 Task 1): a new settlement operator needs partner banks to accept its flows and a regulator to pass its exams. Compliance proof is the door-opener.
- **ChainSentry's binding constraint is a live production reference** — payments is the sector where the corridor money actually moves (Path 2 thesis: licensees must buy AML stacks; a payments operator running us = the reference every other VASP/payment operator respects).
- **The AML hire (Jeffri) lands at the seam** — his JD makes him Fiato's named compliance officer AND ChainSentry's trust authority; he is the human governance layer of this collaboration.
- Timing: his offer targets wk4; Fiato exam-readiness work (gap assessment Day 30) and ChainSentry G1+G2 gate (30 Oct) converge in the same fortnight.

## 3. Collaboration architecture (what each side puts in, gets out)

| | **Fiato Malaysia puts in** | **Fiato Malaysia gets out** |
|---|---|---|
| **Access** | Live transaction flows (screened/aggregated per data-rights annex), compliance policy corpus, licensing posture docs | ChainSentry monitoring, screening & evidence stack at founder-customer terms |
| **People** | Compliance Officer counterpart access (JD §6) | The AML hire as de-facto senior compliance leadership during establishment |
| **Proof** | Logo rights: "running ChainSentry compliance" (written consent per guardrails) | Exam-ready file, partner-bank due-diligence pack, KYB standard |
| **Data** | Historical + live flows to seed monitoring baselines & typology tuning | Real corpus for ChainSentry's payments-leg typology library |

| | **ChainSentry puts in** | **ChainSentry gets out** |
|---|---|---|
| **Stack** | Compliance module suite at founder terms (see §4 scope) | First production deployment + payments-sector case study |
| **People** | AML hire's compliance build-out (JD Task 1 workstreams) | Vetted, exam-hardened product requirements from a live operator |
| **Evidence** | Methodology documentation, monitoring rule transparency | Named reference usable across Path 1–2 pitches ("powering Fiato Malaysia's settlement compliance") |

## 4. Scope of what ChainSentry runs for Fiato (3 modules, frozen — honest-scope rule)

1. **CSF-1 Screen** — sanctions/name/wallet screening on inbound crypto legs + counterparty KYB checks (UN/EU/US + MY designations). Born from Fiato's existing policy §9 commitment; hardened to MY regime.
2. **CSF-2 Monitor** — transaction monitoring + alert triage on settlement flows, typology-tuned (mule chains, scam-centre off-ramping, structuring under MYR thresholds), producing the monitoring-evidence standard Fiato's "continuous monitoring" policy claim requires.
3. **CSF-3 Evidence** — STR-ready case files + regulator/examiner documentation pack + partner-bank due-diligence exports (the exam-ready file and trust kit from JD v4, productized as ChainSentry output).

Anything else (card issuing, FX treasury, custody) is **out of scope** — collaboration dies of success bloat otherwise.

## 5. Pipeline, phased on the AML hire's arrival

### PHASE C-0 — Pre-arrival (now → his Day 1; offer targeted wk4 per master plan)
| Action | Detail | Owner | Gate/status |
|---|---|---|---|
| Joint collaboration term sheet | Bilateral MoU: data rights, consent for use as reference, commercial skeleton (founder terms) — piggybacks the existing data-rights annex (ACT-20260926 family, due 20 Oct) | Vesper draft → Hadri + Fiato sign | Needs Fiato consent + Aras commercial terms [UNKNOWN — see §8] |
| Requirements harvest (raw log) | Fiato compliance gaps + settlement-flow touchpoints logged as candidate CSF-module rows | Vesper | No product promises pre-hire |
| G1+G2 unchanged | Gates 30 Oct stand; Fiato flows enter only AFTER gates pass (no live demo/data before G2 per Gate-Exception Protocol) | Engineering | Blocking dependency for C-1 |
| Fiato licensing posture verification | Confirm the service model + regulator perimeter (BNM e-money/MSB/VA-intermediary — the JD v4 §3 open item) BEFORE flows touch ChainSentry | Vesper OSINT + Hadri/Fiato confirm | Prerequisite, [UNKNOWN] today |

### PHASE C-1 — Day 1→30 (his ramp = joint discovery; converges with P1 Ignition wk5–8)
- His Fiato gap assessment (JD Day-30 measure) doubles as the **CSF-module requirements review**: every gap his assessment finds, ChainSentry screens whether CSF-1/2/3 covers it — misses become backlog, not scope creep.
- His 8 FI interviews scored for payments-sector pull (what settlement operators get asked by partner banks).
- Fiato dogfood begins: compliance calendar + monitoring-evidence standard assembled ON ChainSentry tooling where gates permit; manual where not.
- Data-rights annex finalized BEFORE any live flow moves (blocking precondition).

### PHASE C-2 — Day 30→90 (productize into the pilot; converges P1 late)
- **First live deployment:** CSF-1 Screen + CSF-2 Monitor on Fiato's settlement flows post-gate. This is simultaneously the MY DAX/payments pilot that P0/P1 counts (nominate it to carry the pilot KPI — Dec 4 needed from Hadri).
- **CSF-3's first output:** Fiato's examiner-ready file + first partner-bank due-diligence pack generated BY ChainSentry — the artifact becomes the product's demo asset for every future payments/VASP prospect.
- **TNG Digital brief** rides the same asset: "here is the settlement operator we run compliance for" beats any deck (their Head-of-FCC buying window is open now, ≤6 months).
- Whitepaper positioning: the Fiato deployment is the payments chapter of the methodology whitepaper (MY edition, under the hire's name).

### PHASE C-3 — Day 90→180 (monetize the reference; P2 Scale)
- Founder-customer terms convert to commercial (or the MoU's agreed uplift): first PAYING payments-sector deployment = the cash-bookings KPI gets a real line.
- Reference machinery: Fiato named case study (with written consent) deployed across Path 1 (Luno/MX/Tokenize/TnG displacement doors) and Path 2 (UAE/GCC licensee bundles — a payments operator running ChainSentry is exactly what a new VASP licenseei's compliance officer wants to see).
- Expansion option (needs fresh consent + gate): corridor monitoring for Fiato's international payees = natural second module sale.

## 6. Governance, gates & kill criteria
- **Nothing relaxes:** G1–G6, 01-ACTIVATION-PATHS kill criteria, §9 circuit breakers bind this collaboration; Fiato flows only move post-G2.
- **Collaboration kill criteria (standalone):** (a) Fiato licensing posture unresolved by his Day 45 → descend to CSF-3 evidence-support only, no live monitoring, minute it; (b) no working CSF-1/2 deployment by Day 90 → revert to conventional consultancy support of Fiato's compliance build; ChainSentry reserves reference rights only on delivered artifacts.
- **Conflict-of-interest firewall:** the AML hire wears both hats (JD v4) — employment seat (ChainSentry build) vs Fiato compliance mandate kept separate in contract, data boundary, and sign-off chains (JD §7 guardrails apply verbatim).
- **Records:** collaboration MoU → ART record + DEC at signing; licensing posture finding → INT record; C-phase gates → ACT updates on ACT-20261008-002. All CognitiveOS-governed, PROPOSE → MERGE on Hadri approval.

## 7. Success measures (dated, checkable)
| When | Measure |
|---|---|
| His Day 30 | Gap assessment delivered; CSF-module coverage matrix v1 (covers/not-covers per gap) |
| His Day 45 | Licensing posture resolved (or kill criterion (a) trips) |
| His Day 60 | Data rights finalized; CSF-1+CSF-2 in controlled test on historical flows |
| His Day 90 | Live screening+monitoring on settlement flows; examiner-ready file v1 + first partner-bank DD pack generated by ChainSentry |
| His Day 180 | Commercial conversion signed; named reference live in market; ≥2_Path-2 doors opened citing the Fiato deployment |

## 8. Decisions needed from Hadri (before C-0 spends anything)
1. **Authorize the bilateral MoU draft** — data rights, reference consent, founder-terms commercial skeleton to Fiato.
2. **Confirm Fiato's licensing posture status** (what Fiato believes its MY regulatory perimeter is today — the §C-0 prerequisite).
3. **Nominate the Fiato deployment as the payments pilot** counted in P0/P1 KPIs (Dec 4 in v1 file).
4. **Commercial shape:** founder-terms-free-now / paid-at-Day-180 / equity-or-revenue-share — which skeleton goes in the MoU?

## 9. Verification state
- Fiato entity/service model: fiato.io + /aml_cft crawled 16-Oct [FACT·HIGH]; product stats site-claimed [SITE_ASSERTION].
- Fiato MY licensing posture: **[UNKNOWN]** — Fiato's public footprint says Nigeria entity; Malaysian establishment/licensing status not yet evidenced. Prerequisite confirmation required before C-0 concludes (JD v4 flags the same open item). NOT FOUND ≠ assumption — will be confirmed with Hadri/Fiato directly.
- Hire arrival: ESTIMATE per 02-MASTER-PLAN (offer wk4). H/C-phase anchors to employment Day 1.
- Doctrine quotes: repo files this session. Signals: 2026-10-10 sweep evidence.

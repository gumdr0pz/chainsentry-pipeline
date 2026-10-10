# 03 — KPIs, Risk Register & Open Decisions

**Status:** Canonical v1 (2026-10-08) · Read with `02-MASTER-PLAN.md` calendar; gate values inherit STRATEGY §9.

## 1. KPI tree (Friday one-line log; owner in brackets)

### Level 1 — Program outcomes (board view)
| KPI | Definition | wk4 | wk8 | wk12 | wk26 |
|---|---|---|---|---|---|
| Signed design partners | MOUs w/ data-rights clause | ≥2 | ≥2 | ≥4 | ≥8 (≥3 conversion-committed) |
| Customer-named artifacts | report/reference with *their* name on it | — | ≥1 drafted | ≥1 | ≥2 (1 gov + 1 VASP) |
| Regulator-listed progress | applications accepted / listing achieved | 0 | 1 application | 2 applications | ≥1 in-proc → achieved |
| Cash bookings [EST] | signed ACV (pilots free per strategy) | 0 | 0 | 0–1 | ≥ USD 150k |

### Level 2 — Pipeline health (weekly)
| KPI | Target |
|---|---|
| Seed conversations held (cumulative) | wk4 ≥5 · wk8 ≥12 · wk12 ≥20 |
| Flow-scanner audits delivered (free first-value gift) | ≥1/week after G2 |
| Active pilots | wk8 ≥3 · wk12 ≥8 · wk26 ≥10 |
| Pilot churn/withdrawals | 0 tolerated after wk8 (any churn = interview + minuted cause) |
| Roster coverage: rows with named human + contact (STK records) | ≥50% of Wave-1 rows by wk4; ≥80% by wk12 |
| Inbound share of new meetings (Path 5 evidence pull) | ≥15% by wk16 |

### Level 3 — Product & corpus (gates)
| KPI | Target |
|---|---|
| G1 appliance hardening | wk4 green |
| G2 Reactor/CSV import demo-able (recorded demo exists) | wk2 demo, wk4 gate |
| G3 VASP webhook adapters | ≥2 by wk12 (not 5 — honest re-scope [ASSESSMENT]) |
| G4 court-grade report generator | MY flavour wk10; AE/CH flavours wk20 |
| G5 corpus v0 | labelled/derived ≥10M addresses, one corridor precision measured on pilot feedback, by wk12 |
| Label provenance QA coverage | 100% (AML hire veto live from day one) |
| Sanctions-list refresh latency | <48h from publication |

### Level 4 — Capability & cash discipline
| KPI | Target |
|---|---|
| Seats filled (AML hire / runner) | wk4 offer, wk6 live / wk4 decision, wk6 live |
| Hadri presales load | ≤2 external meetings/week |
| Non-staff cash vs envelope (02 §4) | ≤ envelope at every gate review |
| Register hygiene: KPI Friday-line logged; ACT outcomes merged | weekly, zero skipped weeks |

## 2. Risk register (program-specific; RSK-20261006-001 remains the parent)

| # | Risk | L | I | Mitigation | Trigger → response |
|---|---|---|---|---|---|
| R1 | Pipeline outruns product (parent risk) | M | H | Gate discipline; §7 exception protocol; runner sequencing rule (02 §6) | wk4 G2 red → outreach freeze, product sprint |
| R2 | Seats (AML/runner) unfilled by wk6 → Hadri single-point across 4 timezones | **H** | H | ACT-002 live; runner options A/B/C (D-03); secondment fallback named | wk6 empty → W-2 paperwork-only |
| R3 | Product-engineer availability assumption unverified (inside parent risk) | M | H | Confirm allocation THIS week (D-04) | less than 2 engineers → G2 slips; re-plan P0, tell pilots honestly |
| R4 | JSJK pilot converts to free casework forever (Thai-procurement pattern flagged in strategy) | M | M | Hard conversion clause + data-rights term in every MOU (ACT-008) | pilot end wk90 without conversion paper → escalate to COO, no auto-extend |
| R5 | VARA/SCA turf: Dubai-vs-federal win misread as regime capture | M | M | Two separate relationship tracks; no "we're listed" claims until written | any door conflates them → correct in writing immediately |
| R6 | CH origin-optics: sovereign story misread as BRICS-product story | L | H | Narrative rule enforced (corridor not product); no RU/CN UI association; methodology paper first | any artifact drifts narrative → pull before send |
| R7 | Corpus claim outruns corpus reality in a pitch ("five corridors") | M | H | One-corridor rule (Values §3); precision/recall published even when humble | pitch claims beyond measured corridor → seller correction logged against ACT |
| R8 | Roster burns: named target mishandled in small regulator circle | L | **C** | Policy-grade handling rule; STK hygiene ≥50% wk4; nothing external without epistemic check | any burn → COO-minute, relationship triage that week |
| R9 | Egypt/VN windows close before we're ready (time-limited cohorts) | M | M | Wave W-3 gated on W-1 reference; bundle pack ready wk7 | window passing without reference → let it pass (discipline > FOMO), next cohort exists |
| R10 | FX/procurement cycles (MY JPA/tender, Swiss years) stall conversion math | M | M | Direct-procurement justification early (strategy playbook); CH = 2027 revenue by design | renewal-shaped paper missing wk26 → board sees it in the wk26 verdict |

## 3. Decisions awaiting Hadri (each: recommendation first, default-if-silent)

| # | Decision | Options | Recommendation | Default if silent |
|---|---|---|---|---|
| **D-01** | Ratify Vision/Mission (00) as canonical narrative | approve / amend / reject | **Approve as drafted** (board-deck ready) | suite executes; board deck uses STRATEGY §11 paragraph instead |
| **D-02** | Ratify path portfolio: Path 1+2 primary, 3+4+5 supporting, 6 dark | approve / reshape | **Approve** — matches DEC-20260915-001 + roster logic | run as proposed; paths only change at gate reviews |
| **D-03** | Pipeline-runner staffing route | (a) hire junior BD (b) Aras secondment + commission (c) Faurani practice + MEA contractor | **(b) secondment** — fastest, cash-flat, existing trust | option (c) partial coverage; W-2 paperwork-only persists |
| **D-04** | Confirm product-engineer allocation (2 eng + 1 data through wk4) | confirm / re-scope | **Confirm this week** — it's inside the wk4 gate | plan assumes confirmed; first gate review will expose it — better to know now |
| **D-05** | Corpus seed purchase (~USD 5–25k once) | approve now / hold to wk8 | **Hold to wk8** — buy after first pilot labels arrive, better target | hold (zero-risk default) |
| **D-06** | Salary band + careers contact for JD posting | supply | Supply before wk2 (ACT-002 due 22 Oct) | JD posts "competitive" band; generic inbox risks sourcing quality |
| **D-07** | AML hire vs runner sequencing if only one budget slot exists now | choose | **AML hire first** — lawful pilots gate everything; runner via secondment (D-03b) | AML first |

## 4. Assumptions & epistemic flags (re-verify before external use)

1. `[ASSUMPTION]` Two product engineers + one data person are allocable through wk4 (inside RSK-20261006-001; D-04 forces the check).
2. `[SOURCE_ASSERTION]` Regulatory triggers (SCA first federal licence to Bybit; Paribu–CoinMENA ≤$240M; RAKBANK AED stablecoin AIP; Egypt FRA first approvals; VN pilot-licence track) — news-corroborated 2026-10-06/08; **re-verify anything older than 30 days before it appears in a pitch**.
3. `[EST]` All RM/USD bands (travel, ACV, channel margin, corpus seed, salary) are planning-grade; Aras finance validates P0 envelope at first gate review.
4. `[INFERENCE]` Wave gating, one-corridor discipline, attach-rate targets and inbound-share targets are derived judgments, not measured facts.
5. `[UNKNOWN]` JSJK briefing date, addressee rank (Insp vs ASP), and whether BNM will host a sandbox slot — all flagged where they block; none block suite adoption.
6. `MERGE queue note:` this suite and all ChainSentry OPP-family records sit in register-proposal state until Hadri's MERGE; the repo is the working source of truth meanwhile.

## 5. Friday KPI log (append below, one line per week per 02 §6)

| Week | L1 (signed/named/listed) | L2 (conv·pilots·coverage) | L3 (gates R/Y/G) | L4 (seats·cash) | Note |
|---|---|---|---|---|---|
| wk1 | 0 / 0 / 0 | JSJK reply due; coverage TBD | G2 sprint | JD posted | *first real entry lands fri 10 Oct* |

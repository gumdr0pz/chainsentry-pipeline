# ChainSentry — Plans & Pricing (v1, 2026-10-14)

> Competitive structure benchmarked against MistTrack's published tier ladder (fetched 2026-10-14: Basic $229 / Standard $689 / Compliance $2,069 / Developer from $20/yr / enterprise KYT = contact-us). Structure mirrors the market norm; the **wedge is what MistTrack, Chainalysis and TRM cannot sell: sovereign deployment, corridor-native intelligence, and court-grade auditability at every tier.**
>
> **PENDING-ENGINEERING-CONFIRM tags = proposed numbers, owner may move them. Not capability claims.**

## Tier ladder

| Tier | Price | Buyer | Gates |
|---|---|---|---|
| **Scout** (free) | $0 | Anyone | Wallet risk check, 10 lookups/day — top-of-funnel |
| **Analyst** | **$249/user/mo** | investigators at LEA/FIU/exchange ops | core tracing, 24 chains, corridor labels, 100 lookups/day, 50 monitored addresses |
| **Investigator** | **$749/user/mo** | senior FCC/AML analysts, forensic units | + investigations, DEX & bridge parsing, tracing canvas, OpenAPI, evidence-grade case reports, 5 calls/sec · 25k/day |
| **Compliance** | **$2,299/org/mo** | institutions, VASPs, banks | + KYA/AML batch screening, risk analytics, screening API, immutable audit trail, SSO, priority support |
| **Sovereign** | **Talk to us** (annual/perpetual, node license) | governments, LEAs, national regulators | everything in Compliance **deployed inside your perimeter** — air-gap option, your data residency, your keys, export-controlled-zero |
| **Developer / API** | **from $29/mo**, usage-based | fintechs, on-chain analysts | API-first: risk score, labels, screening endpoints, dashboard-limited |

## What each tier unlocks (feature ladder — same grammar as the market)

**Analyst** — everything to trace money:
- 24 chains GA *(PENDING-ENGINEERING-CONFIRM: final list + count)*
- AML risk score · address labels — **corridor-first: MY/SG/TH/PH/VN/ID/AE/TR/EG exchange, mixer, sanctioned-entity and mule-network label packs**
- Counterparty analysis · transaction actions · address profiles
- 50 monitoring watches · 100 lookups/day · 1 call/sec
- 14-day trial, no card

**Investigator** — everything in Analyst, plus:
- Investigations workspace · DEX & bridge traversal
- Tracing canvas + risk graph
- **Evidence-grade report export** (court/PCAOB-friendly: methodology, hashes, analyst-at-per-action)
- OpenAPI (core endpoints) · 250 watches · 5 calls/sec · 25k calls/day

**Compliance** — everything in Investigator, plus:
- **KYA/AML batch screening** (100k addresses/batch/month *(PENDING-ENGINEERING-CONFIRM)*)
- Risk analytics dashboards · screening API
- Tamper-evident audit log (every query signed) · SSO/SAML · named seats: 10 included
- Priority support, 4h

**Sovereign** — the tier nobody else in this market has:
- Full stack on your bare-metal/VMs, **air-gap install with offline label updates**
- Corridor label packs scoped to your jurisdiction's mandate
- National-case isolation, no phone-home, your HSM/keys
- Deployment engineering + analyst training included *(scope-priced)*
- Auditability aligned to SC/BNM/NACSA expectations and ISO-27001 process evidence
- Licencing: named-node annual or perpetual — procurement-friendly for gov/tender rails

**Developer / API** — from $29/mo (1M calls) *(PENDING-ENGINEERING-CONFIRM)*:
- Risk-score, label, screening endpoints · 99.9% SLA on paid plans *(confirm)*

## Pricing posture (internal — not customer-facing)

- **Never price against Chainalysis on their turf.** We are not "cheaper Chainalysis." SaaS tiers sit at MistTrack ±5% so procurement checklists don't stall; margin and the government story live in **Sovereign** and corridor packs.
- **MY-government angle:** quote in USD with RM invoice via Aras; NACSA licensing gate + ePerolehan/MoF registration path apply *(tracked: ACT-20261010-001, due 31-Oct)*. Local-entity + local-support is a tender-scoring advantage foreign vendors cannot match.
- **Corridor angle (MEA):** VARA/SCA-licensed VASP customers get screening-API bundles; the approved-tooling listing at VARA is distribution, so the SaaS tier is the beachhead there.
- **Kill the discount reflex:** trials and a Standard-style $10/48h probe (copied from MistTrack's hook — converts on upgrade-page intent) replace ad-hoc discounting.

## Trial & commercial policy (published)
- 14-day Analyst trial, full features, no card
- **$10 / 48-hour Investigator probe** — one per account
- Subscriptions non-refundable after first invoice clears (mirrors market norm)
- Annual = 2 months free; seats add at $199/user/mo Analyst/Investigator
- PO/invoice, local entity invoicing (MY), tax invoices under Aras Integrasi Sdn Bhd

## FAQ (published, mirroring MistTrack's page function)
1. **Which chains?** — 24 GA today; corridor chains first on the roadmap; full matrix in docs. *(PENDING-ENGINEERING-CONFIRM before page goes live)*
2. **Is Sovereign really air-gap-capable?** — Yes. Offline bundle updates on signed media; no telemetry required to operate.
3. **Data residency?** — SaaS: AWS ap-southeast region *(confirm)*. Compliance: same + tenancy isolation. Sovereign: your floor, literally.
4. **Court acceptance of reports?** — Reports carry per-action analyst attribution, evidence hashes, and methodology annexes; built for MY court practice first.
5. **API docs?** — public docs site, sandbox keys on all paid tiers.

---
### Source anchors
- MistTrack tier structure/prices: https://misttrack.io/pricing.html fetched 2026-10-14 (Basic $229 · Standard $689 · Compliance $2,069 · Developer from $20/yr · KYT enterprise contact-us · trial hooks 7-day free + $10/48h Standard probe)
- Positioning rules: strategy/STRATEGY.md v2 (commit 2265dca) — deployability · corridor · auditability; never "cheaper Chainalysis"
- Procurement gate: NACSA licence applicability decision due 31-Oct-2026

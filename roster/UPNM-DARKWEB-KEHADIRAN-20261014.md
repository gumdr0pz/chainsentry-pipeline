# Attendance List Extraction — Dark Web Investigation Course

**Source:** photo of sign-in sheet (`img_045ebd7c626b.jpg`, shot rotated 90°)
**Extracted:** 2026-10-15 by Vesper — 5 OCR passes (gateway vision, orientation-corrected, per-row/per-column zoom)
**Confidence:** printed text = high; [?] = handwritten cell genuinely ambiguous in source (do not guess; re-shoot settles it)

## Document header
- **Title:** SENARAI KEHADIRAN PESERTA — DARK WEB INVESTIGATION
- **Date:** 14 OKTOBER 2026 (RABU)
- **Venue:** Kluster Siber, Elektronik dan Robotik, Pusat Kecemerlangan Sultan Ibrahim, UPNM
- **Instruction:** "Lengkapkan maklumat hubungan dan tandatangan bagi mengesahkan kehadiran."
- **Logo:** UPNM
- **Columns:** BIL | PANGKAT DAN NAMA | NO. PERKHIDMATAN | UNIT | NO. TELEFON | EMEL | TANDATANGAN
- **Completeness:** table ends at BIL 5; no further rows, no footer/certification block

## Participants (5 of 5)

| BIL | Rank & Name | Service No. | Unit | Phone | Email | Signed |
|---|---|---|---|---|---|---|
| 1 | Mej Ts. Luqman Hakim bin Ibrahim | 374223 | TUDM — RISUD | 013-399 7[?]50 ⚠ | luqman.hakim@airforce.mil.my ✅hi | ✅ |
| 2 | Mej Muhammad Nabil bin Md Naser | 374339 or 374539 ⚠ | TUDM — RISUD | 019-375 4539 ✅hi | n[?]l.nsr89@gmail.com ⚠ (`nbl.nsr89` most plausible) | ✅ |
| 3 | Kapt Muhammad Rais bin Zakaria | 375795 | TUDM — AWC | 012-703 5791 or 012-303 5797 ⚠ | raiszakaria[96/98]@gmail.com ⚠ | ✅ |
| 4 | Sjn U Mohamad Nazirul Asraf bin Abdullah | 727968 or 727988 ⚠ | TUDM — RISUD | 011-10527908 or …7968 ⚠ | nazirulasraf89@gmail.com (med) | ✅ |
| 5 | Kpl Muhammad Zaim Amsyar bin Mohd Sabri | 740282 | TUDM — RISUD | 011-19180396 (med) | captzaim@gmail.com ✅hi | ✅ |

⚠ = unresolved across passes — cells to verify against paper original.

## Ambiguity ledger (what disagreed between passes)
- Row 1 phone tail: `7370` / `3350` / `7250` readings — unresolved. Email domain settled as `airforce.mil.my` (zoomed EMEL-column pass explicitly confirmed `.mil.my`).
- Row 2 service no. printed `3743 39` vs `3743 59`; phone `019-375 4539` stable.
- Row 3 phone middle digit `7` vs `3`, and email tail `96` vs `98`; stem `raiszakaria` solid.
- Row 4 email `nazirulasraf89` vs `nazrulasraf89` — former matches his name; phone last pair 08 vs 68.
- Row 5 email: early full-frame pass misread `captain@`; corrected-rotation zoom passes converge on `captzaim@gmail.com`.

## Context note (assessment, flagged as such)
Roster skews military cyber-financial: RISUD = Royal Military Forces Finance Corps investigation arm (4 pax), AWC = Air Warfare Centre (1 pax); course subject = dark-web investigation, venue UPNM. ChainSentry ICP-fringe: these are potential cyber-finance crime investigators, i.e. the ICP pattern in uniform. Not yet in the prospect roster; run through contact pipeline (verification states + tiering) on operator go.

---
*Extraction method: vision backend down; recovered via operator AI gateway (Kimi K2.6 vision) through the Harvey brain route. Raw passes reproducible via /tmp/ocr_ccw.py.*
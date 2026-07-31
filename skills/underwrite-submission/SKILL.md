---
name: underwrite-submission
description: End-to-end insurance submission underwriting. Use when reviewing a new or renewal submission, binding a quote package, or walking a risk from intake through decision.
disable-model-invocation: true
---

# Underwrite Submission

Run a disciplined underwriting file: intake → risk → terms → price → authority → decision. This is **decision support**, not a bind authority or legal opinion. Flag uncertainty; never invent facts that are not in the file.

## Inputs to gather (minimum)

- Line(s) of business, effective dates, named insured / operations
- Appetite or guideline source (or state that none was provided)
- Submission materials available (app, SOV, loss runs, financials, loss control, expiring terms)
- Authority / referral rules if known

If critical inputs are missing, run `broker-rfi` for those gaps before deep analysis — unless the user wants a provisional read on what's already present.

## Steps

1. **File map** — List what is in hand vs missing. Note data quality issues (stale loss runs, incomplete SOV, unsigned apps).
2. **Risk picture** — Summarize operations, exposure bases, geographies, and key hazards. Invoke patterns from `hazard-exposure-analysis` and `loss-history-triage` (and `financial-strength-review` when credit/financial strength matters).
3. **Appetite fit** — Apply `risk-appetite-check`. State in / out / borderline with citations to the guideline text you were given.
4. **Terms** — Apply `coverage-terms-review`. Propose structure: limits, deductibles, key exclusions/endorsements, subjectivities.
5. **Price story** — Apply `pricing-rationale`. Separate technical price, marketplace, and credit/debit logic.
6. **Authority** — Apply `referral-authority`. State if the file can clear at desk level or needs referral, and why.
7. **Decision package** — Apply `underwriting-decision-memo`: Quote as presented / Quote with modifications / Decline / Refer. Include subjectivities and next actions.

## Working rules

- Separate **facts**, **inferences**, and **open questions**.
- Prefer tables for exposures, losses, and terms.
- Every adverse finding needs a so-what (why it matters to expected loss or attachment).
- If guidelines conflict with broker narrative, surface the conflict; do not silently prefer either.

**Done when:** the user has a decision recommendation, key drivers, subjectivities/RFIs, and whether referral is required.

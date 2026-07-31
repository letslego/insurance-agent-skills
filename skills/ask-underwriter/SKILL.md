---
name: ask-underwriter
description: Router for insurance underwriting skills. Use when the user is unsure which underwriting workflow to run, or asks what skill fits a submission, renewal, referral, pricing, or decline question.
disable-model-invocation: true
---

# Ask Underwriter

Pick the smallest skill that matches the job. Prefer a focused skill over the full submission flow when the user already knows the question.

## Route

| Situation | Skill |
|-----------|-------|
| Full new/renewal submission end-to-end | `underwrite-submission` |
| Is this in appetite / guideline fit? | `risk-appetite-check` |
| Loss runs, claims trends, large losses | `loss-history-triage` |
| Financials, credit, balance-sheet strength | `financial-strength-review` |
| Locations, COPE, CAT, occupancy, ops hazards | `hazard-exposure-analysis` |
| Forms, limits, deductibles, exclusions, gaps | `coverage-terms-review` |
| Rate, credits/debits, competitive price story | `pricing-rationale` |
| Needs referral? Within authority? | `referral-authority` |
| Quote / modify / decline memo | `underwriting-decision-memo` |
| Missing info / broker questions | `broker-rfi` |
| Expiring vs proposed terms | `renewal-comparison` |

## Steps

1. Restate the user's goal in one sentence (line of business, new vs renewal if known).
2. Name **one** primary skill and, if useful, one follow-on skill.
3. Ask only for the minimum inputs that skill needs if they are missing.
4. Offer to run the primary skill next.

**Done when:** the user has a clear next skill and knows what to provide.

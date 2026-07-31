---
name: risk-appetite-check
description: Check a risk against underwriting appetite and guidelines. Use when asking if a class, industry, geography, or account is in appetite, prohibited, or referral-only.
---

# Risk Appetite Check

Map the risk to **in appetite**, **out of appetite**, **referral**, or **insufficient information** using only the appetite/guideline source provided (or explicitly mark assumptions if the user asks for a provisional view).

## Steps

1. Confirm LOB, class/NAICS or operations narrative, geography, size metrics (TIV, revenue, payroll, vehicles, headcount, etc.).
2. Extract the relevant appetite rules: preferred, acceptable, prohibited, capacity caps, mandatory referrals.
3. Score each material attribute:
   - **Fit** — aligns with preferred/acceptable
   - **Friction** — acceptable but needs controls, pricing, or terms
   - **Break** — prohibited or exceeds hard stop
4. Produce a verdict table: attribute → rule cited → status → implication.
5. State overall posture: **Pursue** / **Pursue with modification** / **Refer** / **Decline** / **Need info**.

## Output shape

```
Verdict: …
Drivers (max 5): …
Hard stops: …
Referral triggers: …
Info gaps blocking a firm call: …
```

**Done when:** every material appetite attribute is classified and the overall posture is unambiguous.

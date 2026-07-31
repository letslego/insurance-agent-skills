---
name: financial-strength-review
description: Review insured financial strength for underwriting. Use when analyzing financials, credit risk, bankruptcy risk, or ability to fund retentions and risk control.
---

# Financial Strength Review

Assess whether the insured can support the risk transfer structure (retention, collateral, long-tail liability, growth). Not a formal credit rating.

## Steps

1. Identify statements available (audit vs management, years, consolidated vs entity).
2. Snapshot: revenue trend, profitability, liquidity, leverage, net worth, cash flow.
3. Stress the retention: can they fund the deductible/SIR after a bad year?
4. Flag reds: going-concern language, covenant pressure, related-party dependence, rapid leverage, unpaid loss obligations, thin captive funding if relevant.
5. Tie financial posture to structure: lower SIR, collateral, parent guarantee, shorter term, decline credit-sensitive covers.

## Output shape

- **Strength posture:** Strong / Adequate / Weak / Unknown
- **Key ratios / facts** (only from provided numbers)
- **Retention affordability**
- **Structure implications**
- **Info gaps**

**Done when:** posture and structure implications are explicit, with numbers cited from the file.

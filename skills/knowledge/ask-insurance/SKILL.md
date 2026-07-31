---
name: ask-insurance
description: Router for all insurance desk skills. Use when unsure which insurance skill to run across underwriting, claims, customer, compliance, or analytics.
disable-model-invocation: true
---

# Ask Insurance

Pick the smallest skill that matches the job across the whole desk.

## Route

| Situation | Skill |
|-----------|-------|
| Unsure which UW skill | `ask-underwriter` |
| Full UW submission | `underwrite-submission` |
| New claim intake | `fnol-intake` |
| Is it covered? | `coverage-determination` |
| Who's at fault? | `liability-assessment` |
| Repair vs total / track | `severity-triage` |
| Suspicious claim patterns | `fraud-red-flags` |
| Recovery from third party | `subrogation-scan` |
| Customer claim update | `claims-status-update` |
| Why is my price this? | `quote-explanation` |
| What coverages should I buy? | `coverage-counseling` |
| Add driver/car/address | `endorsement-impact` |
| Angry customer / supervisor | `complaint-escalation` |
| About to cancel | `retention-save` |
| MVR/CLUE review | `mvr-clue-review` |
| Driving score / UBI | `telematics-review` |
| Bundle / household | `household-risk` |
| Non-renew explanation | `nonrenew-rationale` |
| DOI complaint | `regulatory-complaint-response` |
| Fair claims audit | `fair-claims-check` |
| Shop estimate dispute | `repair-network-qa` |
| Call/chat QA | `interaction-qa-scoring` |
| Rate filing story | `rate-filing-narrative` |
| LR went bad | `loss-ratio-investigation` |
| Storm / CAT ops | `catastrophe-event-brief` |
| Cite the manual | `guideline-cite` |
| Teach from a case | `agent-coaching` |
| Hand off a case | `handoff-brief` |

## Steps

1. Restate the user's goal in one sentence.
2. Name one primary skill and optional follow-on.
3. Ask only for missing critical inputs.
4. Offer to run the primary skill next.

**Done when:** the user has a clear next skill.

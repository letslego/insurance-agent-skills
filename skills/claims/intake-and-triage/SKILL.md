---
name: intake-and-triage
description: End-to-end claim intake and triage agent. Use when opening a new claim, stitching FNOL intake with coverage verification, fraud screening, and route/escalate decisions.
disable-model-invocation: true
---

# Intake and Triage

Run a complete **intake-and-triage** loop for a new claim:

**collect claim details → verify coverage → detect fraud signals → route / escalate**

This is decision support. Do not invent policy wording, accuse fraud, or bind coverage. Separate **facts**, **inferences**, and **open questions**.

## Inputs to gather (minimum)

- Loss narrative (call/chat notes, customer statement, or FNOL form)
- Policy identifiers and any forms/declarations available
- Carrier guidelines for coverage, SIU referral, and assignment (or mark provisional)

If the file is too thin to triage, still run intake, then produce a blocker list and stop before a firm route.

## Steps (invoke these skills in order)

1. **Collect claim details** — Run `fnol-intake`.
   - Completion: structured FNOL summary, parties/units, immediate needs, missing facts.
2. **Verify coverage** — Run `coverage-determination` on the FNOL facts + policy materials.
   - Completion: covered / not covered / partial / investigate, with cited gaps.
3. **Detect fraud signals** — Run `fraud-red-flags` on the same file.
   - Completion: clear / monitor / refer to SIU, with factual indicators only.
4. **Route / escalate** — Run `severity-triage`, then `handoff-brief` when ownership leaves the intake desk.
   - Choose the handling track (glass/low, repair, total, injury/complex, SIU, coverage counsel).
   - If SIU or coverage counsel is required, escalate with a crisp ask and due timing.
5. **Package the triage decision** — Produce the intake-and-triage summary below.

Optional follow-ons (only if needed): `liability-assessment`, `claims-status-update`, `subrogation-scan`.

## Output shape

```
Claim / policy refs:
FNOL abstract:
Coverage posture: … (drivers)
Fraud posture: clear | monitor | SIU refer (indicators)
Severity / handling track:
Route decision: desk adjuster | DRP/field | SIU | coverage counsel | supervisor
Escalation ask (if any):
Subjectivities / missing facts:
Next owner + due:
Customer-safe next-step line:
```

## Pairing map

| Step | Skill | Why |
|------|-------|-----|
| Intake | `fnol-intake` | Capture a usable loss notice |
| Coverage | `coverage-determination` | Map facts to policy posture |
| Fraud | `fraud-red-flags` | SIU screen without accusations |
| Track | `severity-triage` | Repair / total / complex path |
| Escalate | `handoff-brief` | Clean transfer with landmines called out |

**Done when:** the claim has a coverage posture, fraud posture, handling track, and a named next owner (or a blocker list that explains why triage cannot finish).

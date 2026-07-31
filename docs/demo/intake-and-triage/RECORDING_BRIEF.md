# Recording brief — Intake & triage workflow demo

Target length: **6–9 minutes**. Destination: GitHub Pages **Workflows** section.

## Storyboard

| # | Shot | On screen | Voiceover point |
|---|------|-----------|-----------------|
| 1 | Title | “Intake & triage workflow” | What we’re building: collect → coverage → fraud → route |
| 2 | Install (Claude Code) | `/plugin marketplace add` → install → `/reload-plugins` | One-time install |
| 3 | Confirm skills | Slash menu shows `/intake-and-triage`, `/fnol-intake`, etc. | Pack is live |
| 4 | Open sample | `SAMPLE_CLAIM.md` | Fictional claim; messy real-world intake |
| 5 | Run orchestrator | Paste demo prompt, invoke `/intake-and-triage` | Stitching, not one giant freeform prompt |
| 6 | Step A | Agent runs `/fnol-intake` output | Collect details |
| 7 | Step B | `/coverage-determination` | Verify coverage |
| 8 | Step C | `/fraud-red-flags` | Fraud signals / SIU posture |
| 9 | Step D | `/severity-triage` + `/handoff-brief` | Route / escalate |
| 10 | Recap | Final triage package on screen | How the four capabilities map to skills |
| 11 | CTA | Docs URL + workflow chain | Viewers can replay the same prompt |

## What the recorder must capture

1. **Real UI** — Claude Code *or* Cursor Agent chat (pick one; don’t switch mid-video).
2. **Real install** — marketplace add + plugin install (or `npx skills` if Cursor-only).
3. **Real model responses** — do not paste pre-written answers into the agent as if it generated them.
4. **Mic audio** — quiet room; or we can lay studio voiceover on a silent screen capture using the script below.

## Narration script (studio VO option)

**Intro.**  
In this demo we’ll install Insurance Agent Skills, then stitch a workflow for an intake-and-triage agent: collect claim details, verify coverage, detect fraud signals, and route or escalate.

**Install.**  
In Claude Code, add the letslego insurance-agent-skills marketplace, install the insurance-agent-skills plugin, and reload plugins. You should see slash commands like intake-and-triage and fnol-intake.

**Setup.**  
We’ll use a fictional sample claim — messy call notes plus a short policy excerpt — the kind of incomplete file intake teams actually see.

**Run.**  
We invoke intake-and-triage and ask the agent to show which skill it uses at each step.

**Collect.**  
First, fnol-intake turns the messy notes into a structured loss notice: parties, damage, missing facts, immediate needs.

**Verify.**  
Next, coverage-determination maps those facts to the policy excerpt — comprehensive versus collision posture, deductible, rental limits, and what still needs verification.

**Fraud.**  
Then fraud-red-flags screens for SIU indicators — date inconsistency, thin third-party identity, prior phone-number collision — and recommends clear, monitor, or refer, without accusing the customer.

**Route.**  
Severity-triage picks the handling track; handoff-brief packages the escalation if SIU or a specialist owner is needed.

**Close.**  
That’s the stitch: four capabilities, five focused skills, one orchestrator. Replay it from the Workflows section on the docs site.

## Files ready in repo

- Orchestrator skill: `skills/claims/intake-and-triage/`
- Sample claim: `docs/demo/intake-and-triage/SAMPLE_CLAIM.md`
- This brief: `docs/demo/intake-and-triage/RECORDING_BRIEF.md`

# Deploy at scale — sample code

Companion samples for the [Deploy at scale](../../README.md#deploy-at-scale) guide. Each folder maps to one step.

| Step | Folder | What it shows |
|------|--------|----------------|
| 1. Package & pin | [`01-package-pin/`](./01-package-pin) | Pin a git tag, install skills, promote a desk allowlist |
| 2. Orchestrate | [`02-orchestrate/`](./02-orchestrate) | Cursor Agent CLI worker + TypeScript SDK-style runner |
| 3. Ground truth | [`03-ground-truth/`](./03-ground-truth) | Build a run context from manuals, authority, allowlists |
| 4. Rollout rings | [`04-rollout-rings/`](./04-rollout-rings) | Pilot → shadow → assist → automate gate |
| 5. Operate | [`05-operate/`](./05-operate) | Eval golden files, audit log, simple guardrails |
| 6. Write back | [`06-writeback/`](./06-writeback) | Parse triage package → mock claims-core API |

These are **illustrative**. Swap stubs for your CMS, queue, and claims/UW systems. Do not treat outputs as binding authority.

## Quick start (offline)

No agent API required — exercises rings, guardrails, parse, mock writeback, and audit:

```bash
CLAIM_ID=demo-001 bash examples/deploy-at-scale/end-to-end.sh \
  examples/deploy-at-scale/fixtures/sample-triage-package.md
```

Eval golden files:

```bash
python3 examples/deploy-at-scale/05-operate/eval_suite.py \
  --golden-dir examples/deploy-at-scale/05-operate/golden \
  --outputs-dir examples/deploy-at-scale/05-operate/golden
```

Live agent path (needs Cursor Agent auth + pinned skills in the workspace):

```bash
# 1) pin pack into a workspace (use an immutable git tag in prod)
PACK_REF=main DESK=claims-intake TARGET_DIR=/path/to/workspace \
  bash examples/deploy-at-scale/01-package-pin/install-pinned.sh

# 2–3) ground truth + orchestrator
CONTEXT_DIR=examples/deploy-at-scale/03-ground-truth/carrier-context.example \
  bash examples/deploy-at-scale/03-ground-truth/run-with-context.sh path/to/fnol.md
```

Pinning clones `PACK_REF` (tag/branch/sha) then runs `npx skills add <checkout> --agent cursor -y --skill '*'`.  
Do **not** use `org/repo@tag` with the skills CLI — `@` selects a skill name, not a git ref.

Optional: `pip install pyyaml` if you prefer `rings.yaml` over `rings.json`.

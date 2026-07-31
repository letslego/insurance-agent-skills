#!/usr/bin/env bash
# Step 2 — Orchestrate via Cursor Agent CLI (batch / queue worker pattern).
# Requires: agent CLI authenticated (CURSOR_API_KEY or `agent login`).
# Workspace must already have pinned skills under .agents/skills/ (see 01-package-pin).
set -euo pipefail

WORKSPACE="${WORKSPACE:-$(pwd)}"
CLAIM_FILE="${1:?Usage: $0 <path-to-fnol.md|json> [output.md]}"
OUT="${2:-${WORKSPACE}/.runs/triage-$(basename "$CLAIM_FILE").md}"
mkdir -p "$(dirname "$OUT")"

PROMPT=$(cat <<EOF
Run the intake-and-triage skill on this FNOL package.
Produce a complete triage package (all required sections).
Do not invent coverage, policy numbers, or guideline citations.
Cite only manuals present under docs/agents/ or carrier-context/.

FNOL / claim package path: ${CLAIM_FILE}
EOF
)

echo "==> Orchestrator: intake-and-triage"
echo "    workspace: ${WORKSPACE}"
echo "    claim:     ${CLAIM_FILE}"
echo "    output:    ${OUT}"

# --print streams the final agent response; pin model if your org requires it
agent --print \
  --workspace "$WORKSPACE" \
  --force \
  --output-format text \
  "$PROMPT" | tee "$OUT"

echo "==> Wrote ${OUT}"

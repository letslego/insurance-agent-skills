#!/usr/bin/env bash
# Step 3 — Build ground truth, then call the Step 2 orchestrator.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
CONTEXT_DIR="${CONTEXT_DIR:-$ROOT/carrier-context.example}"
CLAIM_FILE="${1:?Usage: $0 <fnol-file>}"
CLAIM_ID="${CLAIM_ID:-demo-001}"
SKILL="${SKILL:-intake-and-triage}"
WORKSPACE="${WORKSPACE:-$(pwd)}"
RUN_DIR="${WORKSPACE}/.runs"
mkdir -p "$RUN_DIR"

python3 "$ROOT/build-run-context.py" \
  --context-dir "$CONTEXT_DIR" \
  --skill "$SKILL" \
  --claim-id "$CLAIM_ID" \
  --out "$RUN_DIR/carrier-context-${CLAIM_ID}.md"

# Prepend context into a combined prompt file for the worker
COMBINED="$RUN_DIR/prompt-${CLAIM_ID}.md"
{
  echo "# Use this carrier context as ground truth"
  echo
  cat "$RUN_DIR/carrier-context-${CLAIM_ID}.md"
  echo
  echo "# FNOL package"
  echo
  cat "$CLAIM_FILE"
} > "$COMBINED"

bash "$ROOT/../02-orchestrate/run-intake-cli.sh" "$COMBINED" "$RUN_DIR/triage-${CLAIM_ID}.md"

#!/usr/bin/env bash
# Glue script: steps 3→4→5→6 on an existing triage markdown (or generate context only).
# For a full live agent run, use 03-ground-truth/run-with-context.sh first.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
CLAIM_ID="${CLAIM_ID:-demo-001}"
PACKAGE_MD="${1:?Usage: $0 <triage-package.md>}"
WORKSPACE="${WORKSPACE:-$(pwd)}"
RUN_DIR="${WORKSPACE}/.runs"
mkdir -p "$RUN_DIR"

# 4) Ring decision
RING_JSON="$RUN_DIR/ring-${CLAIM_ID}.json"
python3 "$ROOT/04-rollout-rings/ring_router.py" \
  --rings "$ROOT/04-rollout-rings/rings.yaml" \
  --claim-id "$CLAIM_ID" | tee "$RING_JSON"

# 5) Guardrails
python3 "$ROOT/05-operate/guardrails.py" "$PACKAGE_MD" --json | tee "$RUN_DIR/guardrails-${CLAIM_ID}.json"
python3 "$ROOT/05-operate/guardrails.py" "$PACKAGE_MD"

# 6) Parse + writeback according to ring mode
TRIAGE_JSON="$RUN_DIR/triage-${CLAIM_ID}.json"
python3 "$ROOT/06-writeback/parse_triage.py" "$PACKAGE_MD" --out "$TRIAGE_JSON"

MODE=$(python3 -c "import json;print(json.load(open('$RING_JSON')).get('writeback','none'))")
# Re-run ring with structured triage for automate decisions
python3 "$ROOT/04-rollout-rings/ring_router.py" \
  --rings "$ROOT/04-rollout-rings/rings.yaml" \
  --claim-id "$CLAIM_ID" \
  --triage-json "$TRIAGE_JSON" | tee "$RING_JSON"
MODE=$(python3 -c "import json;m=json.load(open('$RING_JSON')).get('writeback','none');print(m if m in ('draft_only','auto_route_low_risk') else 'none')")

python3 "$ROOT/06-writeback/claims_core_client.py" \
  --claim-id "$CLAIM_ID" \
  --triage-json "$TRIAGE_JSON" \
  --package-md "$PACKAGE_MD" \
  --mode "${MODE:-none}"

# 5) Audit
PACK_VERSION=$(python3 -c "import json,pathlib;p=pathlib.Path('.agents/pack-pin.json');print(json.load(open(p))['version'] if p.is_file() else 'unpinned')")
python3 "$ROOT/05-operate/audit_log.py" \
  --claim-id "$CLAIM_ID" \
  --skill intake-and-triage \
  --pack-version "$PACK_VERSION" \
  --ring "$(python3 -c "import json;print(json.load(open('$RING_JSON'))['ring'])")" \
  --output-file "$PACKAGE_MD" \
  --log "$RUN_DIR/audit.jsonl"

echo "==> Done. Artifacts under ${RUN_DIR}"

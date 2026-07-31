#!/usr/bin/env bash
# Step 1 — Package once, pin versions.
# Clone an exact git ref, install into the workspace, prune to a desk allowlist.
#
# Note: `npx skills add org/repo@name` means skill *name*, not a git tag.
# Pinning is done by cloning PACK_REF (tag/branch/sha) then installing from disk.
set -euo pipefail

PACK_REPO="${PACK_REPO:-letslego/insurance-agent-skills}"
PACK_REF="${PACK_REF:-${PACK_TAG:-main}}"   # prefer an immutable tag in prod
TARGET_DIR="${TARGET_DIR:-.}"
DESK="${DESK:-claims-intake}"
PROMOTED_FILE="${PROMOTED_FILE:-$(cd "$(dirname "$0")" && pwd)/promoted-skills.json}"
AGENT="${AGENT:-cursor}"
CACHE_ROOT="${SKILLS_PIN_CACHE:-${TMPDIR:-/tmp}/skills-pin-cache}"
CACHE="${CACHE_ROOT}/${PACK_REPO//\//__}/${PACK_REF}"

echo "==> Pinning ${PACK_REPO}@${PACK_REF} into ${TARGET_DIR} (desk=${DESK})"

if [[ ! -d "${CACHE}/.git" ]]; then
  mkdir -p "$(dirname "$CACHE")"
  echo "==> Cloning ${PACK_REPO} @ ${PACK_REF}"
  if ! git clone --depth 1 --branch "$PACK_REF" "https://github.com/${PACK_REPO}.git" "$CACHE" 2>/tmp/skills-pin-clone.err; then
    # Fallback for bare SHAs or when --branch is unsupported
    git clone --depth 1 "https://github.com/${PACK_REPO}.git" "$CACHE"
    git -C "$CACHE" fetch --depth 1 origin "$PACK_REF"
    git -C "$CACHE" checkout "$PACK_REF"
  fi
else
  echo "==> Reusing cached checkout ${CACHE}"
fi

PIN_SHA="$(git -C "$CACHE" rev-parse HEAD)"
mkdir -p "$TARGET_DIR"
cd "$TARGET_DIR"

echo "==> Installing skills from pinned checkout (${PIN_SHA:0:12})"
npx --yes skills@latest add "$CACHE" --agent "$AGENT" -y --skill '*'

if command -v python3 >/dev/null && [[ -f "$PROMOTED_FILE" ]]; then
  python3 - "$PROMOTED_FILE" "$DESK" "$PACK_REPO" "$PACK_REF" "$PIN_SHA" <<'PY'
import json, shutil, sys
from pathlib import Path

promoted_path, desk, pack, ref, sha = sys.argv[1:6]
cfg = json.loads(Path(promoted_path).read_text())
if desk not in cfg["desks"]:
    raise SystemExit(f"Unknown desk '{desk}'. Choose from: {', '.join(cfg['desks'])}")
allowed = set(cfg["desks"][desk]["skills"])
root = Path(".agents/skills")
if not root.is_dir():
    raise SystemExit("No .agents/skills directory after install")

pruned = []
for skill_dir in list(root.iterdir()):
    if not skill_dir.is_dir():
        continue
    if skill_dir.name not in allowed:
        print(f"prune unpromoted: {skill_dir.name}")
        shutil.rmtree(skill_dir)
        pruned.append(skill_dir.name)

kept = sorted(p.name for p in root.iterdir() if p.is_dir())
missing = sorted(allowed - set(kept))
if missing:
    print(f"WARNING: promoted skills missing from pack: {', '.join(missing)}")

Path(".agents/pack-pin.json").write_text(json.dumps({
    "pack": pack,
    "version": ref,
    "commit": sha,
    "desk": desk,
    "skills": kept,
    "pruned": sorted(pruned),
}, indent=2) + "\n")
print(f"Pinned {pack}@{ref} ({sha[:12]}) desk={desk} kept={len(kept)} pruned={len(pruned)}")
PY
fi

echo "==> Done. See .agents/pack-pin.json"

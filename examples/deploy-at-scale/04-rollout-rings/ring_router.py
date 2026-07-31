#!/usr/bin/env python3
"""Step 4 — Assign a claim to a rollout ring and decide writeback mode."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None


def load_rings(path: Path) -> dict:
    text = path.read_text()
    if path.suffix == ".json":
        return json.loads(text)
    if yaml:
        return yaml.safe_load(text)
    # Prefer sibling rings.json when PyYAML is unavailable
    sibling = path.with_suffix(".json")
    if sibling.is_file():
        return json.loads(sibling.read_text())
    raise SystemExit("Install PyYAML or pass --rings rings.json")


def stable_bucket(claim_id: str, salt: str = "intake-and-triage") -> int:
    h = hashlib.sha256(f"{salt}:{claim_id}".encode()).hexdigest()
    return int(h[:8], 16) % 100


def pick_ring(cfg: dict, claim_id: str) -> tuple[str, dict]:
    if cfg.get("kill_switch"):
        return "killed", {"mode": "off", "reason": "kill_switch"}

    bucket = stable_bucket(claim_id, cfg.get("workflow", "wf"))
    # Walk rings in rollout order; first matching enabled band wins
    order = ["pilot", "shadow", "assist", "automate"]
    cursor = 0
    for name in order:
        ring = (cfg.get("rings") or {}).get(name) or {}
        if not ring.get("enabled"):
            continue
        width = int(ring.get("traffic_percent") or 0)
        if cursor <= bucket < cursor + width:
            return name, ring
        cursor += width
    return "control", {"mode": "human_only", "reason": "outside_rings"}


def decide_automate(ring: dict, triage: dict) -> str:
    """Return writeback action for automate ring."""
    rules = ring.get("auto_route_when") or {}
    severity = (triage.get("severity") or "").lower()
    fraud_n = int(triage.get("fraud_indicator_count") or 0)
    coverage_clear = bool(triage.get("coverage_clear"))

    max_sev = (rules.get("max_severity") or "minor").lower()
    sev_rank = {"minor": 0, "moderate": 1, "major": 2, "critical": 3}
    if sev_rank.get(severity, 99) > sev_rank.get(max_sev, 0):
        return "escalate_via_handoff_brief"
    if fraud_n > int(rules.get("max_fraud_indicators") or 0):
        return "escalate_via_handoff_brief"
    if rules.get("coverage_clear") and not coverage_clear:
        return "escalate_via_handoff_brief"
    return ring.get("writeback") or "auto_route_low_risk"


def main() -> int:
    ap = argparse.ArgumentParser()
    default_rings = Path(__file__).with_name("rings.json")
    if not default_rings.is_file():
        default_rings = Path(__file__).with_name("rings.yaml")
    ap.add_argument("--rings", type=Path, default=default_rings)
    ap.add_argument("--claim-id", required=True)
    ap.add_argument("--triage-json", type=Path, help="Optional structured triage summary")
    args = ap.parse_args()

    cfg = load_rings(args.rings)
    name, ring = pick_ring(cfg, args.claim_id)
    decision = {
        "claim_id": args.claim_id,
        "ring": name,
        "mode": ring.get("mode", "off"),
        "pack_tag": cfg.get("pinned_pack_tag"),
    }

    if name == "automate" and args.triage_json and args.triage_json.is_file():
        triage = json.loads(args.triage_json.read_text())
        decision["writeback"] = decide_automate(ring, triage)
    elif name in {"assist", "pilot"}:
        decision["writeback"] = ring.get("writeback", "draft_only")
    elif name == "shadow":
        decision["writeback"] = "none_score_only"
        decision["score_skills"] = ring.get("score_skills", [])
    else:
        decision["writeback"] = "none"

    print(json.dumps(decision, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

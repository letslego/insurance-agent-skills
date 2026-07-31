#!/usr/bin/env python3
"""Step 5 — Append-only audit + telemetry record for one agent run."""
from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path


def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--log", type=Path, default=Path(".runs/audit.jsonl"))
    ap.add_argument("--claim-id", required=True)
    ap.add_argument("--skill", required=True)
    ap.add_argument("--pack-version", required=True)
    ap.add_argument("--model", default="unknown")
    ap.add_argument("--ring", default="unknown")
    ap.add_argument("--latency-ms", type=int, default=0)
    ap.add_argument("--prompt-file", type=Path)
    ap.add_argument("--output-file", type=Path)
    ap.add_argument("--escalated", action="store_true")
    ap.add_argument("--overridden", action="store_true")
    args = ap.parse_args()

    prompt = args.prompt_file.read_text() if args.prompt_file and args.prompt_file.is_file() else ""
    output = args.output_file.read_text() if args.output_file and args.output_file.is_file() else ""

    # PII-light telemetry: hashes + lengths, not raw bodies (store bodies in secure store)
    record = {
        "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "claim_id": args.claim_id,
        "skill": args.skill,
        "pack_version": args.pack_version,
        "model": args.model,
        "ring": args.ring,
        "latency_ms": args.latency_ms,
        "prompt_sha256": sha256_text(prompt) if prompt else None,
        "output_sha256": sha256_text(output) if output else None,
        "prompt_chars": len(prompt),
        "output_chars": len(output),
        "escalated": args.escalated,
        "overridden": args.overridden,
    }

    args.log.parent.mkdir(parents=True, exist_ok=True)
    with args.log.open("a") as f:
        f.write(json.dumps(record) + "\n")
    print(json.dumps(record, indent=2))


if __name__ == "__main__":
    main()

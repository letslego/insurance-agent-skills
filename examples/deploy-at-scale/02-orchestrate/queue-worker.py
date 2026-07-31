#!/usr/bin/env python3
"""Step 2 — Thin queue worker: claim_id → orchestrator CLI → handoff path.

Replace dequeue()/ack() with SQS, Kafka, Azure Queue, etc.
"""
from __future__ import annotations

import json
import os
import subprocess
import tempfile
from pathlib import Path

WORKSPACE = Path(os.environ.get("WORKSPACE", ".")).resolve()
CLI = Path(__file__).with_name("run-intake-cli.sh")


def dequeue() -> dict | None:
    """Stub: one message from stdin JSON line, or None when done."""
    line = os.environ.get("CLAIM_MESSAGE")
    if not line:
        return None
    return json.loads(line)


def fetch_fnol(claim_id: str) -> str:
    """Stub: load FNOL text for claim_id from your core system."""
    sample = WORKSPACE / "docs" / "demo" / "intake-and-triage" / "sample-claim.md"
    if sample.is_file():
        return sample.read_text()
    return f"# FNOL\nClaim ID: {claim_id}\n(replace with core API payload)\n"


def ack(claim_id: str, out_path: Path) -> None:
    print(json.dumps({"acked": claim_id, "handoff": str(out_path)}))


def main() -> None:
    msg = dequeue()
    if not msg:
        print("No CLAIM_MESSAGE; nothing to do")
        return

    claim_id = msg["claim_id"]
    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as f:
        f.write(fetch_fnol(claim_id))
        fnol_path = f.name

    out = WORKSPACE / ".runs" / f"triage-{claim_id}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        ["bash", str(CLI), fnol_path, str(out)],
        check=True,
        env={**os.environ, "WORKSPACE": str(WORKSPACE)},
    )
    ack(claim_id, out)


if __name__ == "__main__":
    main()

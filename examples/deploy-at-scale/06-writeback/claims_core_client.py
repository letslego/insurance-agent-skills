#!/usr/bin/env python3
"""Step 6 — Mock claims-core writeback (draft vs auto-route).

Replace MockClaimsCore with your real API client.
"""
from __future__ import annotations

import argparse
import json
import urllib.error
import urllib.request
from pathlib import Path


class MockClaimsCore:
    def __init__(self, base_url: str | None = None):
        self.base_url = (base_url or "").rstrip("/")
        self.local_store = Path(".runs/writeback.jsonl")

    def _post(self, path: str, payload: dict) -> dict:
        if not self.base_url:
            self.local_store.parent.mkdir(parents=True, exist_ok=True)
            with self.local_store.open("a") as f:
                f.write(json.dumps({"path": path, "payload": payload}) + "\n")
            return {"ok": True, "mode": "mock_local", "path": path}
        req = urllib.request.Request(
            f"{self.base_url}{path}",
            data=json.dumps(payload).encode(),
            headers={"Content-Type": "application/json"},
            method="POST",
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.URLError as e:
            return {"ok": False, "error": str(e)}

    def draft_triage(self, claim_id: str, triage: dict, package_md: str) -> dict:
        return self._post(
            f"/claims/{claim_id}/triage/draft",
            {"triage": triage, "package_markdown": package_md, "status": "pending_human"},
        )

    def auto_route(self, claim_id: str, triage: dict, queue: str) -> dict:
        return self._post(
            f"/claims/{claim_id}/route",
            {"triage": triage, "queue": queue, "status": "auto_routed"},
        )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--claim-id", required=True)
    ap.add_argument("--triage-json", type=Path, required=True)
    ap.add_argument("--package-md", type=Path, required=True)
    ap.add_argument("--mode", choices=["draft_only", "auto_route_low_risk", "none"], required=True)
    ap.add_argument("--base-url", default="")
    args = ap.parse_args()

    triage = json.loads(args.triage_json.read_text())
    package = args.package_md.read_text()
    client = MockClaimsCore(args.base_url or None)

    if args.mode == "none":
        print(json.dumps({"ok": True, "skipped": True}))
        return 0
    if args.mode == "draft_only":
        result = client.draft_triage(args.claim_id, triage, package)
    else:
        queue = triage.get("recommended_handoff") or "fnol-standard"
        result = client.auto_route(args.claim_id, triage, queue)

    print(json.dumps(result, indent=2))
    return 0 if result.get("ok", True) else 1


if __name__ == "__main__":
    raise SystemExit(main())

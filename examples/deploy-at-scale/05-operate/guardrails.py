#!/usr/bin/env python3
"""Step 5 — Lightweight output guardrails before writeback."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

BIND_DENY = re.compile(
    r"\b(coverage (is )?denied|we (are )?(denying|binding)|policy is bound|bind the risk)\b",
    re.I,
)
FRAUD_ACCUSATION = re.compile(
    r"\b(you (committed|are committing) fraud|fraudulent claim|liar)\b",
    re.I,
)
CITATION = re.compile(
    r"(manual|guideline|form|endorsement|§|needs verification)",
    re.I,
)


def check(text: str) -> list[dict]:
    findings = []
    if BIND_DENY.search(text) and not CITATION.search(text):
        findings.append(
            {
                "rule": "no_bind_deny_without_citation",
                "severity": "block",
                "detail": "Bind/deny language without guideline citation",
            }
        )
    if FRAUD_ACCUSATION.search(text):
        findings.append(
            {
                "rule": "fraud_indicators_only",
                "severity": "block",
                "detail": "Accusation language; fraud skills must stay indicators-only",
            }
        )
    return findings


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("output_file", type=Path)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    text = args.output_file.read_text()
    findings = check(text)
    payload = {"ok": not findings, "findings": findings}
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        if findings:
            for f in findings:
                print(f"[{f['severity']}] {f['rule']}: {f['detail']}", file=sys.stderr)
        else:
            print("guardrails ok")
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())

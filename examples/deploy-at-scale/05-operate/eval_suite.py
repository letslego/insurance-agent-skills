#!/usr/bin/env python3
"""Step 5 — Eval suite: golden expectations vs agent output markdown."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


def has_section(text: str, title: str) -> bool:
    # Match markdown headings or bold labels loosely
    pattern = re.compile(rf"(^|\n)\s*#+\s*{re.escape(title)}|(\*\*|__)?{re.escape(title)}(\*\*|__)?\s*:?", re.I)
    return bool(pattern.search(text))


def citation_ok(text: str) -> bool:
    if re.search(r"needs verification|cannot determine|missing policy", text, re.I):
        return True
    return bool(
        re.search(r"(manual|guideline|form|endorsement|§|section)\s+[\w.-]+", text, re.I)
    )


def evaluate(expect: dict, output: str) -> list[str]:
    failures: list[str] = []
    for sec in expect.get("required_sections") or []:
        if not has_section(output, sec):
            # also allow case-insensitive substring as soft pass for demos
            if sec.lower() not in output.lower():
                failures.append(f"missing section: {sec}")
    for phrase in expect.get("must_not_contain") or []:
        if phrase.lower() in output.lower():
            failures.append(f"forbidden phrase: {phrase}")
    if expect.get("citation_rule") and re.search(r"coverage", output, re.I):
        if not citation_ok(output):
            failures.append("citation_rule failed for coverage language")
    return failures


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--golden-dir", type=Path, default=Path(__file__).with_name("golden"))
    ap.add_argument("--outputs-dir", type=Path, required=True)
    ap.add_argument("--report", type=Path, help="Write JSON report")
    args = ap.parse_args()

    results = []
    failed = 0
    for expect_path in sorted(args.golden_dir.glob("*.expect.json")):
        expect = json.loads(expect_path.read_text())
        out_path = args.outputs_dir / f"{expect['id']}.md"
        if not out_path.is_file():
            # also try triage- prefix
            alt = args.outputs_dir / f"triage-{expect['id']}.md"
            out_path = alt if alt.is_file() else out_path
        if not out_path.is_file():
            results.append({"id": expect["id"], "ok": False, "failures": ["missing output file"]})
            failed += 1
            continue
        failures = evaluate(expect, out_path.read_text())
        ok = not failures
        if not ok:
            failed += 1
        results.append({"id": expect["id"], "ok": ok, "failures": failures, "file": str(out_path)})

    report = {"passed": len(results) - failed, "failed": failed, "cases": results}
    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())

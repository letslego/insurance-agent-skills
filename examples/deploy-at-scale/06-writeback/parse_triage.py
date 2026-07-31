#!/usr/bin/env python3
"""Step 6 — Parse a triage markdown package into structured fields for core systems."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


SECTION_RE = re.compile(r"^#{1,3}\s+(.+)$", re.M)


def split_sections(text: str) -> dict[str, str]:
    matches = list(SECTION_RE.finditer(text))
    sections: dict[str, str] = {}
    for i, m in enumerate(matches):
        title = m.group(1).strip()
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        sections[title.lower()] = text[start:end].strip()
    return sections


def first_match(patterns: list[str], text: str) -> str | None:
    for pat in patterns:
        m = re.search(pat, text, re.I | re.M)
        if m:
            return (m.group(1) if m.lastindex else m.group(0)).strip()
    return None


def parse(text: str) -> dict:
    sections = split_sections(text)
    blob = text
    severity = first_match(
        [
            r"severity\s*[:\-]\s*(minor|moderate|major|critical)",
            r"\b(minor|moderate|major|critical)\b.*severity",
        ],
        blob,
    )
    fraud_lines = [
        ln.strip("-* ").strip()
        for key, body in sections.items()
        if "fraud" in key
        for ln in body.splitlines()
        if ln.strip().startswith(("-", "*"))
    ]
    coverage_clear = bool(
        re.search(r"coverage\s+(appears\s+)?(clear|likely|confirmed)", blob, re.I)
    ) and not re.search(r"uncertain|needs verification|cannot determine", blob, re.I)

    handoff = first_match(
        [
            r"handoff\s+to\s*[:\-]\s*(\S+)",
            r"recommended\s+handoff\s*[:\-]\s*(\S+)",
            r"recommend(?:ed)?\s+queue\s*[:\-]\s*(\S+)",
        ],
        blob,
    )

    return {
        "severity": (severity or "unknown").lower(),
        "fraud_indicator_count": len(fraud_lines),
        "fraud_indicators": fraud_lines[:20],
        "coverage_clear": coverage_clear,
        "recommended_handoff": handoff,
        "sections_found": sorted(sections.keys()),
        "raw_chars": len(text),
    }


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("triage_md", type=Path)
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()
    data = parse(args.triage_md.read_text())
    text = json.dumps(data, indent=2)
    print(text)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text + "\n")


if __name__ == "__main__":
    main()

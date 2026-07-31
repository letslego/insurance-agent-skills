#!/usr/bin/env python3
"""Step 3 — Inject carrier ground truth into every agent run.

Builds a single markdown context file the orchestrator prompt can include,
and validates the requested skill against the desk allowlist.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    import yaml  # type: ignore
except ImportError:
    yaml = None


def load_authority(path: Path) -> dict:
    text = path.read_text()
    if path.suffix in {".yaml", ".yml"}:
        if yaml is None:
            # Minimal fallback for the example file (no nested complexity)
            data: dict = {"skills_allowed": []}
            for line in text.splitlines():
                s = line.strip()
                if s.startswith("- ") and "skills_allowed" not in s:
                    # collect list items after we saw skills_allowed
                    pass
            # Prefer PyYAML; if missing, parse skills_allowed naively
            in_skills = False
            skills = []
            for line in text.splitlines():
                if line.strip().startswith("skills_allowed:"):
                    in_skills = True
                    continue
                if in_skills:
                    if line.startswith("  - "):
                        skills.append(line.strip()[2:].strip())
                    elif line and not line.startswith(" "):
                        break
            data = {"skills_allowed": skills, "raw": text}
            return data
        return yaml.safe_load(text)
    return json.loads(text)


def main() -> int:
    p = argparse.ArgumentParser(description="Build ground-truth context for one run")
    p.add_argument("--context-dir", type=Path, required=True)
    p.add_argument("--skill", required=True, help="Orchestrator or skill name")
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--claim-id", default="unknown")
    args = p.parse_args()

    ctx = args.context_dir
    authority_path = ctx / "authority-matrix.yaml"
    if not authority_path.is_file():
        authority_path = ctx / "authority-matrix.yml"
    authority = load_authority(authority_path) if authority_path.is_file() else {}
    allowed = set(authority.get("skills_allowed") or [])

    if allowed and args.skill not in allowed:
        print(
            f"REJECTED: skill '{args.skill}' not in desk allowlist: {sorted(allowed)}",
            file=sys.stderr,
        )
        return 2

    parts = [
        f"# Carrier run context",
        f"",
        f"- claim_id: `{args.claim_id}`",
        f"- skill: `{args.skill}`",
        f"- desk allowlist: {', '.join(sorted(allowed)) or '(none configured)'}",
        f"",
        f"## Authority matrix",
        f"",
        authority_path.read_text() if authority_path.is_file() else "_(missing)_",
        f"",
    ]

    for name in ("claims-manual-excerpt.md", "pii-rules.md"):
        path = ctx / name
        if path.is_file():
            parts += [f"## {name}", "", path.read_text(), ""]

    # Optional RAG dump: concatenate any extra *.md under manuals/
    manuals = ctx / "manuals"
    if manuals.is_dir():
        parts.append("## Additional manuals")
        parts.append("")
        for md in sorted(manuals.glob("**/*.md")):
            parts += [f"### {md.relative_to(ctx)}", "", md.read_text(), ""]

    parts += [
        "## Instructions to the agent",
        "",
        "- Treat the authority matrix and manuals as ground truth.",
        "- Use `/guideline-cite` style citations; do not invent form names.",
        "- Fraud skills: indicators only — never accuse.",
        "- No bind/deny language without a citation to the manuals above.",
        "",
    ]

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("\n".join(parts))
    print(f"Wrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

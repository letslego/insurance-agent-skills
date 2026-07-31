#!/usr/bin/env python3
"""Build a narrated explainer video for Insurance Agent Skills."""

from __future__ import annotations

import asyncio
import json
import subprocess
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
import edge_tts

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "video"
SLIDES = OUT / "slides"
AUDIO = OUT / "audio"
WORK = OUT / "work"

INK = (11, 61, 92)
INK_DEEP = (7, 42, 64)
TEAL = (47, 111, 106)
COPPER = (196, 92, 38)
PAPER = (238, 242, 244)
WHITE = (247, 250, 251)
MUTED = (77, 100, 115)

W, H = 1920, 1080
VOICE = "en-US-AndrewNeural"

PACK_ORDER = [
    "knowledge",
    "underwriting",
    "claims",
    "customer",
    "personal-lines",
    "compliance",
    "analytics",
]

PACK_LABELS = {
    "knowledge": "Knowledge & routing",
    "underwriting": "Underwriting",
    "claims": "Claims",
    "customer": "Customer & sales",
    "personal-lines": "Personal lines",
    "compliance": "Compliance & QA",
    "analytics": "Analytics & ops",
}

# Curated pairings: skill -> list of complementary skills
PAIRINGS = {
    "ask-insurance": ["ask-underwriter", "fnol-intake", "quote-explanation"],
    "guideline-cite": ["ask-insurance", "risk-appetite-check", "fair-claims-check"],
    "agent-coaching": ["interaction-qa-scoring", "handoff-brief", "complaint-escalation"],
    "handoff-brief": ["underwrite-submission", "fnol-intake", "complaint-escalation"],
    "ask-underwriter": ["underwrite-submission", "ask-insurance"],
    "underwrite-submission": [
        "risk-appetite-check",
        "loss-history-triage",
        "pricing-rationale",
        "underwriting-decision-memo",
    ],
    "risk-appetite-check": ["underwrite-submission", "referral-authority", "guideline-cite"],
    "loss-history-triage": ["pricing-rationale", "underwrite-submission", "hazard-exposure-analysis"],
    "financial-strength-review": ["coverage-terms-review", "underwrite-submission"],
    "hazard-exposure-analysis": ["coverage-terms-review", "pricing-rationale", "catastrophe-event-brief"],
    "coverage-terms-review": ["pricing-rationale", "underwriting-decision-memo", "broker-rfi"],
    "pricing-rationale": ["renewal-comparison", "underwriting-decision-memo", "risk-appetite-check"],
    "referral-authority": ["underwriting-decision-memo", "handoff-brief"],
    "underwriting-decision-memo": ["broker-rfi", "referral-authority", "underwrite-submission"],
    "broker-rfi": ["underwrite-submission", "coverage-terms-review"],
    "renewal-comparison": ["pricing-rationale", "coverage-terms-review", "nonrenew-rationale"],
    "fnol-intake": ["coverage-determination", "severity-triage", "fraud-red-flags"],
    "coverage-determination": ["liability-assessment", "claims-status-update", "guideline-cite"],
    "liability-assessment": ["subrogation-scan", "severity-triage", "claims-status-update"],
    "severity-triage": ["repair-network-qa", "claims-status-update", "fnol-intake"],
    "fraud-red-flags": ["handoff-brief", "fnol-intake", "liability-assessment"],
    "subrogation-scan": ["liability-assessment", "handoff-brief"],
    "claims-status-update": ["complaint-escalation", "coverage-determination"],
    "quote-explanation": ["coverage-counseling", "retention-save", "endorsement-impact"],
    "coverage-counseling": ["quote-explanation", "endorsement-impact", "household-risk"],
    "endorsement-impact": ["mvr-clue-review", "quote-explanation", "risk-appetite-check"],
    "complaint-escalation": ["claims-status-update", "retention-save", "regulatory-complaint-response"],
    "retention-save": ["quote-explanation", "coverage-counseling", "handoff-brief"],
    "mvr-clue-review": ["risk-appetite-check", "nonrenew-rationale", "telematics-review"],
    "telematics-review": ["quote-explanation", "mvr-clue-review", "pricing-rationale"],
    "household-risk": ["coverage-counseling", "underwrite-submission", "retention-save"],
    "nonrenew-rationale": ["renewal-comparison", "mvr-clue-review", "guideline-cite"],
    "regulatory-complaint-response": ["fair-claims-check", "complaint-escalation", "handoff-brief"],
    "fair-claims-check": ["claims-status-update", "regulatory-complaint-response"],
    "repair-network-qa": ["severity-triage", "claims-status-update"],
    "interaction-qa-scoring": ["agent-coaching", "complaint-escalation"],
    "rate-filing-narrative": ["loss-ratio-investigation", "guideline-cite"],
    "loss-ratio-investigation": ["rate-filing-narrative", "pricing-rationale", "catastrophe-event-brief"],
    "catastrophe-event-brief": ["fnol-intake", "hazard-exposure-analysis", "claims-status-update"],
}


def load_skills() -> list[dict]:
    data = (ROOT / "docs" / "skills-data.js").read_text()
    raw = data.split("=", 1)[1].strip()
    if raw.endswith(";"):
        raw = raw[:-1]
    skills = json.loads(raw)
    by_pack: dict[str, list] = {p: [] for p in PACK_ORDER}
    for s in skills:
        by_pack.setdefault(s["pack"], []).append(s)
    ordered = []
    for pack in PACK_ORDER:
        ordered.extend(by_pack.get(pack, []))
    return ordered


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    candidates = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial Bold.ttf" if bold else "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    for path in candidates:
        try:
            return ImageFont.truetype(path, size=size)
        except Exception:
            continue
    return ImageFont.load_default()


def wrap(text: str, width: int) -> list[str]:
    return textwrap.wrap(text, width=width) or [""]


def draw_bg(draw: ImageDraw.ImageDraw) -> None:
    draw.rectangle((0, 0, W, H), fill=PAPER)
    # subtle header bar
    draw.rectangle((0, 0, W, 12), fill=INK)
    draw.rectangle((0, H - 18, W, H), fill=TEAL)


def draw_brand(draw: ImageDraw.ImageDraw, subtitle: str = "") -> None:
    draw.text((80, 48), "Insurance Agent Skills", fill=INK, font=font(36, bold=True))
    if subtitle:
        draw.text((80, 100), subtitle, fill=TEAL, font=font(28, bold=True))


def save_slide(name: str, draw_fn) -> Path:
    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    draw_bg(draw)
    draw_fn(draw)
    path = SLIDES / f"{name}.png"
    img.save(path, "PNG")
    return path


def title_slide() -> Path:
    def _draw(d: ImageDraw.ImageDraw):
        d.text((80, 280), "Insurance Agent Skills", fill=INK_DEEP, font=font(92, bold=True))
        for i, line in enumerate(
            wrap(
                "A guided tour of all 39 skills — when to use each one, and how to pair them on a real insurance desk.",
                48,
            )
        ):
            d.text((80, 430 + i * 56), line, fill=MUTED, font=font(40))
        d.text((80, 720), "Claude Code  ·  Codex  ·  Cursor", fill=COPPER, font=font(34, bold=True))

    return save_slide("000_title", _draw)


def pack_slide(idx: str, pack: str, count: int) -> Path:
    label = PACK_LABELS.get(pack, pack)

    def _draw(d: ImageDraw.ImageDraw):
        draw_brand(d, "Skill pack")
        d.text((80, 320), label, fill=INK_DEEP, font=font(88, bold=True))
        d.text((80, 450), f"{count} skills in this section", fill=MUTED, font=font(40))
        tip = {
            "knowledge": "Start here when you are unsure which skill to run.",
            "underwriting": "Use for submissions, renewals, appetite, price, and decisions.",
            "claims": "Use from first notice of loss through recovery and updates.",
            "customer": "Use for quotes, coverage choices, complaints, and saves.",
            "personal-lines": "Use for MVR/CLUE, telematics, households, and non-renewals.",
            "compliance": "Use for regulator responses, fair-claims audits, and QA.",
            "analytics": "Use for filings, loss-ratio diagnosis, and catastrophe briefs.",
        }.get(pack, "")
        for i, line in enumerate(wrap(tip, 52)):
            d.text((80, 560 + i * 48), line, fill=TEAL, font=font(36))

    return save_slide(f"{idx}_pack_{pack}", _draw)


def skill_slide(idx: str, skill: dict) -> Path:
    pairs = PAIRINGS.get(skill["id"], [])
    pair_text = ", ".join(f"/{p}" for p in pairs[:4]) if pairs else "/ask-insurance"

    def _draw(d: ImageDraw.ImageDraw):
        draw_brand(d, PACK_LABELS.get(skill["pack"], skill["pack"]))
        d.text((80, 180), skill["name"], fill=INK_DEEP, font=font(64, bold=True))
        d.text((80, 265), skill["command"], fill=COPPER, font=font(36, bold=True))

        d.text((80, 360), "WHEN TO USE", fill=TEAL, font=font(28, bold=True))
        y = 410
        for line in wrap(skill["when"], 56):
            d.text((80, y), line, fill=MUTED, font=font(34))
            y += 44

        d.text((80, y + 30), "PAIR WITH", fill=TEAL, font=font(28, bold=True))
        y += 80
        for line in wrap(pair_text, 56):
            d.text((80, y), line, fill=INK, font=font(34, bold=True))
            y += 44

        d.text((80, 960), skill["blurb"][:110], fill=MUTED, font=font(26))

    return save_slide(f"{idx}_{skill['id']}", _draw)


def closing_slide() -> Path:
    def _draw(d: ImageDraw.ImageDraw):
        d.text((80, 280), "Start with /ask-insurance", fill=INK_DEEP, font=font(72, bold=True))
        lines = [
            "Install from letslego/insurance-agent-skills,",
            "keep your carrier guidelines in context,",
            "and chain focused skills instead of one giant prompt.",
            "",
            "Docs: letslego.github.io/insurance-agent-skills",
        ]
        for i, line in enumerate(lines):
            d.text((80, 420 + i * 52), line, fill=MUTED, font=font(36))

    return save_slide("999_closing", _draw)


def install_slide() -> Path:
    def _draw(d: ImageDraw.ImageDraw):
        draw_brand(d, "Install")
        d.text((80, 220), "How to install", fill=INK_DEEP, font=font(72, bold=True))
        blocks = [
            ("Claude Code", "/plugin marketplace add letslego/insurance-agent-skills"),
            ("", "/plugin install insurance-agent-skills@insurance-agent-skills"),
            ("Codex / Cursor", "npx skills@latest add letslego/insurance-agent-skills"),
            ("Then", "Run /ask-insurance to route to the right skill."),
        ]
        y = 360
        for label, text in blocks:
            if label:
                d.text((80, y), label, fill=TEAL, font=font(32, bold=True))
                y += 48
            d.text((80, y), text, fill=INK, font=font(34))
            y += 58

    return save_slide("001_install", _draw)


def narration_for_skill(skill: dict) -> str:
    pairs = PAIRINGS.get(skill["id"], [])
    if pairs:
        pair_phrase = ", ".join(pairs[:3])
        pair_sentence = f" Pair it with {pair_phrase}."
    else:
        pair_sentence = " Pair it with ask-insurance if you need a broader route."
    when = skill["when"].rstrip(".")
    return (
        f"{skill['name']}. "
        f"Use this when {when[0].lower() + when[1:]}. "
        f"{skill['blurb']} "
        f"{pair_sentence}"
    )


def narration_for_pack(pack: str, count: int) -> str:
    label = PACK_LABELS.get(pack, pack)
    tips = {
        "knowledge": "These skills help you route work, cite manuals, coach people, and hand off cases cleanly.",
        "underwriting": "These skills walk a submission from appetite and exposure through price, authority, and a written decision.",
        "claims": "These skills cover intake, coverage, liability, severity, fraud screening, recovery, and customer updates.",
        "customer": "These skills help explain price, counsel on coverages, handle endorsements, de-escalate complaints, and save policies.",
        "personal-lines": "These skills interpret reports, telematics, household risk, and non-renewal rationale.",
        "compliance": "These skills support regulator responses, fair-claims audits, repair-network QA, and interaction scoring.",
        "analytics": "These skills turn exhibits and results into filing narratives, loss-ratio diagnosis, and catastrophe briefs.",
    }
    return f"Next, {label}. {count} skills. {tips.get(pack, '')}"


async def synthesize(text: str, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(str(path))


def ffprobe_duration(path: Path) -> float:
    out = subprocess.check_output(
        [
            "ffprobe",
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=noprint_wrappers=1:nokey=1",
            str(path),
        ],
        text=True,
    ).strip()
    return float(out)


def render_clip(slide: Path, audio: Path, out: Path, min_seconds: float = 2.5) -> None:
    duration = max(ffprobe_duration(audio) + 0.35, min_seconds)
    subprocess.check_call(
        [
            "ffmpeg",
            "-y",
            "-loop",
            "1",
            "-i",
            str(slide),
            "-i",
            str(audio),
            "-c:v",
            "libx264",
            "-tune",
            "stillimage",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-pix_fmt",
            "yuv420p",
            "-shortest",
            "-t",
            f"{duration:.3f}",
            "-vf",
            "scale=1920:1080",
            str(out),
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


async def main() -> None:
    for d in (OUT, SLIDES, AUDIO, WORK):
        d.mkdir(parents=True, exist_ok=True)

    skills = load_skills()
    segments: list[tuple[str, Path, str]] = []

    # Build slides + narration texts
    segments.append(("000_title", title_slide(), 
        "Welcome to Insurance Agent Skills. This video walks through all thirty-nine skills: "
        "when to use each one, and how to pair it with other skills on a real insurance desk."
    ))
    segments.append(("001_install", install_slide(),
        "To install in Claude Code, add the letslego insurance-agent-skills marketplace, "
        "install the insurance-agent-skills plugin, and reload plugins. "
        "In Codex or Cursor, run npx skills latest add letslego insurance-agent-skills. "
        "After install, start with ask-insurance."
    ))

    by_pack: dict[str, list] = {}
    for s in skills:
        by_pack.setdefault(s["pack"], []).append(s)

    n = 2
    for pack in PACK_ORDER:
        pack_skills = by_pack.get(pack, [])
        if not pack_skills:
            continue
        idx = f"{n:03d}"
        segments.append((f"{idx}_pack_{pack}", pack_slide(idx, pack, len(pack_skills)), narration_for_pack(pack, len(pack_skills))))
        n += 1
        for skill in pack_skills:
            idx = f"{n:03d}"
            segments.append((f"{idx}_{skill['id']}", skill_slide(idx, skill), narration_for_skill(skill)))
            n += 1

    segments.append(("999_closing", closing_slide(),
        "That is the full Insurance Agent Skills pack. Start with ask-insurance, "
        "keep your carrier guidelines in context, and chain focused skills instead of one giant prompt. "
        "Documentation lives at letslego dot github dot i o slash insurance-agent-skills."
    ))

    print(f"Generating {len(segments)} narrated segments…")
    clip_paths = []
    for i, (key, slide, text) in enumerate(segments, 1):
        audio_path = AUDIO / f"{key}.mp3"
        clip_path = WORK / f"{key}.mp4"
        print(f"[{i}/{len(segments)}] {key}")
        await synthesize(text, audio_path)
        render_clip(slide, audio_path, clip_path)
        clip_paths.append(clip_path)

    concat_list = WORK / "concat.txt"
    concat_list.write_text("".join(f"file '{p.resolve()}'\n" for p in clip_paths))
    final = OUT / "insurance-agent-skills-tour.mp4"
    subprocess.check_call(
        [
            "ffmpeg",
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(concat_list),
            "-c",
            "copy",
            str(final),
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    # Also export a compact script for reference
    script_path = OUT / "narration-script.md"
    lines = ["# Insurance Agent Skills — Narration Script\n"]
    for key, _, text in segments:
        lines.append(f"## {key}\n\n{text}\n")
    script_path.write_text("\n".join(lines))

    print(f"Wrote {final}")
    print(f"Duration ~{sum(ffprobe_duration(p) for p in clip_paths)/60:.1f} minutes")


if __name__ == "__main__":
    asyncio.run(main())

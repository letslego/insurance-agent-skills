#!/usr/bin/env python3
"""Build intake-and-triage workflow demo video from a live agent transcript + studio VO."""

from __future__ import annotations

import asyncio
import subprocess
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
import edge_tts

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "video" / "workflow-intake-triage"
SLIDES = OUT / "slides"
AUDIO = OUT / "vo"
WORK = OUT / "work"
AGENT_OUT = OUT / "agent-output.txt"
FINAL = OUT / "intake-and-triage-workflow-demo.mp4"

INK = (11, 61, 92)
INK_DEEP = (7, 42, 64)
TEAL = (47, 111, 106)
COPPER = (196, 92, 38)
PAPER = (238, 242, 244)
MUTED = (77, 100, 115)
TERM_BG = (18, 28, 36)
TERM_FG = (220, 232, 238)
TERM_DIM = (120, 140, 150)
TERM_ACCENT = (120, 220, 180)

W, H = 1920, 1080
VOICE = "en-US-AndrewNeural"


def font(size: int, bold: bool = False):
    paths = [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf" if bold else "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial Bold.ttf" if bold else "/Library/Fonts/Arial.ttf",
    ]
    for p in paths:
        try:
            return ImageFont.truetype(p, size=size)
        except Exception:
            pass
    return ImageFont.load_default()


def wrap(text: str, width: int):
    return textwrap.wrap(text, width=width) or [""]


def save(name: str, draw_fn) -> Path:
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    d.rectangle((0, 0, W, 12), fill=INK)
    d.rectangle((0, H - 16, W, H), fill=TEAL)
    draw_fn(d)
    path = SLIDES / f"{name}.png"
    path.parent.mkdir(parents=True, exist_ok=True)
    img.save(path)
    return path


def title_slide():
    def _d(d):
        d.text((80, 240), "Workflow demo", fill=TEAL, font=font(36, True))
        d.text((80, 320), "Intake & triage agent", fill=INK_DEEP, font=font(78, True))
        for i, line in enumerate(
            wrap(
                "Live Cursor agent run: install skills, then stitch FNOL → coverage → fraud → route/escalate.",
                48,
            )
        ):
            d.text((80, 460 + i * 52), line, fill=MUTED, font=font(36))
        d.text((80, 700), "Silent capture  ·  Studio voiceover", fill=COPPER, font=font(32, True))

    return save("00_title", _d)


def install_slide():
    def _d(d):
        d.text((80, 80), "Step 1 — Install in Cursor", fill=INK_DEEP, font=font(56, True))
        # terminal panel
        d.rounded_rectangle((80, 200, W - 80, H - 120), radius=18, fill=TERM_BG)
        lines = [
            "$ cd intake-triage-demo",
            "$ npx skills@latest add letslego/insurance-agent-skills --yes",
            "",
            "✔ Installing skills for Cursor…",
            "✔ intake-and-triage",
            "✔ fnol-intake",
            "✔ coverage-determination",
            "✔ fraud-red-flags",
            "✔ severity-triage",
            "✔ handoff-brief",
            "",
            "$ find .agents/skills -name SKILL.md",
        ]
        y = 240
        for line in lines:
            color = TERM_ACCENT if line.startswith("✔") or line.startswith("$") else TERM_FG
            d.text((120, y), line, fill=color, font=font(30))
            y += 42

    return save("01_install", _d)


def sample_slide():
    def _d(d):
        d.text((80, 80), "Step 2 — Sample claim file", fill=INK_DEEP, font=font(56, True))
        d.rounded_rectangle((80, 180, W - 80, H - 100), radius=18, fill=TERM_BG)
        body = Path("/Users/amitabhakarmakar/Projects/intake-triage-demo/SAMPLE_CLAIM.md").read_text()
        y = 220
        for line in body.splitlines()[:18]:
            d.text((120, y), line[:100], fill=TERM_FG if not line.startswith("#") else TERM_ACCENT, font=font(26))
            y += 36

    return save("02_sample", _d)


def chain_slide():
    def _d(d):
        d.text((80, 80), "Step 3 — Stitch the workflow", fill=INK_DEEP, font=font(56, True))
        steps = [
            ("1", "fnol-intake", "Collect claim details"),
            ("2", "coverage-determination", "Verify coverage"),
            ("3", "fraud-red-flags", "Detect fraud signals"),
            ("4", "severity-triage", "Choose handling track"),
            ("5", "handoff-brief", "Route / escalate"),
        ]
        y = 220
        for num, cmd, label in steps:
            d.rounded_rectangle((80, y, W - 80, y + 110), radius=14, fill=(247, 250, 251))
            d.ellipse((110, y + 28, 170, y + 88), fill=TEAL)
            d.text((128, y + 40), num, fill=PAPER, font=font(32, True))
            d.text((210, y + 28), f"/{cmd}", fill=COPPER, font=font(34, True))
            d.text((210, y + 70), label, fill=MUTED, font=font(28))
            y += 130
        d.text((80, 980), "Orchestrator: /intake-and-triage", fill=INK, font=font(30, True))

    return save("03_chain", _d)


def terminal_slide(name: str, title: str, lines: list[str]):
    def _d(d):
        d.text((80, 60), title, fill=INK_DEEP, font=font(44, True))
        d.rounded_rectangle((80, 140, W - 80, H - 80), radius=18, fill=TERM_BG)
        d.text((120, 170), "cursor-agent — live run", fill=TERM_DIM, font=font(24))
        y = 220
        for line in lines[-18:]:
            text = line[:108]
            color = TERM_ACCENT if text.startswith("##") or text.startswith("**") or text.startswith("/") else TERM_FG
            d.text((120, y), text, fill=color, font=font(26))
            y += 36
            if y > H - 120:
                break

    return save(name, _d)


def closing_slide():
    def _d(d):
        d.text((80, 280), "Workflow complete", fill=INK_DEEP, font=font(72, True))
        for i, line in enumerate(
            [
                "Install once → invoke /intake-and-triage →",
                "the agent stitches focused skills instead of one giant prompt.",
                "",
                "Replay materials: docs/demo/intake-and-triage/",
            ]
        ):
            d.text((80, 420 + i * 52), line, fill=MUTED, font=font(34))

    return save("99_closing", _d)


async def synth(text: str, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    await edge_tts.Communicate(text, VOICE).save(str(path))


def duration(path: Path) -> float:
    out = subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=noprint_wrappers=1:nokey=1", str(path)],
        text=True,
    ).strip()
    return float(out)


def render_clip(slide: Path, audio: Path, out: Path):
    dur = max(duration(audio) + 0.4, 2.5)
    subprocess.check_call(
        [
            "ffmpeg", "-y", "-loop", "1", "-i", str(slide), "-i", str(audio),
            "-c:v", "libx264", "-tune", "stillimage", "-c:a", "aac", "-b:a", "192k",
            "-pix_fmt", "yuv420p", "-shortest", "-t", f"{dur:.3f}",
            str(out),
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )


def chunk_transcript(text: str) -> list[tuple[str, str, list[str], str]]:
    """Return (slide_name, title, lines, narration) chunks from agent output."""
    lines = [ln.rstrip() for ln in text.splitlines() if ln.strip()]
    if not lines:
        lines = ["(Agent output missing — rerun capture)"]

    def section(start: str, end: str | None = None) -> list[str]:
        capturing = False
        out = []
        for ln in lines:
            if start in ln:
                capturing = True
            if capturing and end and end in ln and out:
                break
            if capturing:
                out.append(ln)
        return out or lines[:12]

    chunks = [
        (
            "10_fnol",
            "Live agent — /fnol-intake",
            section("Step 1", "Step 2"),
            "The Cursor agent starts with fnol-intake. It turns messy call notes into a structured loss notice: "
            "who called, where it happened, the Civic damage, the thinly identified other driver, and the missing facts — "
            "especially the Friday-to-Saturday date correction and photos that never arrived.",
        ),
        (
            "11_coverage",
            "Live agent — /coverage-determination",
            section("Step 2", "Step 3"),
            "Next, coverage-determination maps those facts to the policy excerpt. "
            "The vehicle and named insured match, but the exact loss date still needs confirmation. "
            "Rental exists on the policy, yet the car is driveable, so rental is conditional. "
            "The agent marks coverage as investigate — not invented wording.",
        ),
        (
            "12_fraud",
            "Live agent — /fraud-red-flags",
            section("Step 3", "Step 4"),
            "Then fraud-red-flags screens for SIU indicators without accusing anyone: "
            "the date change, napkin phone and missing insurance card, the unverified phone-number collision with another claim, "
            "and missing photos. Recommendation: monitor, and prepare an SIU refer only if the phone flag confirms.",
        ),
        (
            "13_route",
            "Live agent — /severity-triage + /handoff-brief",
            section("Step 4", "Final intake"),
            "Severity-triage classifies this as a moderate repair on a driveable car — desk or D R P photo estimate. "
            "Handoff-brief routes ownership to the claim adjuster within one business day, with SIU on standby if the phone flag verifies, "
            "and a customer-safe next step: send photos and confirm the loss date.",
        ),
        (
            "14_package",
            "Live agent — final triage package",
            section("Final intake", None),
            "The orchestrator finishes with one package: coverage posture, fraud posture, handling track, route decision, "
            "and the stitch itself — fnol-intake, to coverage-determination, to fraud-red-flags, to severity-triage, to handoff-brief, "
            "under intake-and-triage.",
        ),
    ]
    return chunks


async def main():
    for d in (OUT, SLIDES, AUDIO, WORK):
        d.mkdir(parents=True, exist_ok=True)

    transcript = AGENT_OUT.read_text() if AGENT_OUT.exists() else ""
    segments: list[tuple[Path, str]] = []

    segments.append((title_slide(),
        "This is a live Cursor workflow demo for an intake-and-triage agent. "
        "We install Insurance Agent Skills, open a sample claim, and stitch focused skills: "
        "collect details, verify coverage, detect fraud signals, then route or escalate."))
    segments.append((install_slide(),
        "First, in the Cursor workspace, install the public pack with npx skills add letslego insurance-agent-skills. "
        "That places intake-and-triage and its child skills where Cursor can load them."))
    segments.append((sample_slide(),
        "We use a fictional sample claim: messy call notes, a partial plate, a date correction, "
        "and a phone number that collided with another claim — exactly the kind of incomplete file intake teams see."))
    segments.append((chain_slide(),
        "The orchestrator is intake-and-triage. It stitches fnol-intake, coverage-determination, "
        "fraud-red-flags, severity-triage, and handoff-brief — instead of one giant freeform prompt."))

    for name, title, lines, narr in chunk_transcript(transcript):
        segments.append((terminal_slide(name, title, lines), narr))

    segments.append((closing_slide(),
        "That's the stitch. Install once, invoke intake-and-triage, and let the agent walk collect, verify, screen, and route. "
        "You can replay the sample claim from the Workflows section on the docs site."))

    print(f"Building {len(segments)} clips…")
    clips = []
    for i, (slide, text) in enumerate(segments):
        audio = AUDIO / f"{i:02d}.mp3"
        clip = WORK / f"{i:02d}.mp4"
        print(f"[{i+1}/{len(segments)}] {slide.name}")
        await synth(text, audio)
        render_clip(slide, audio, clip)
        clips.append(clip)

    concat = WORK / "concat.txt"
    concat.write_text("".join(f"file '{c.resolve()}'\n" for c in clips))
    subprocess.check_call(
        ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat), "-c", "copy", str(FINAL)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    print("Wrote", FINAL)
    print(f"Duration ~{sum(duration(c) for c in clips)/60:.1f} min")


if __name__ == "__main__":
    asyncio.run(main())

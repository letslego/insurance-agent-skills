# Skills tour video

Narrated explainer covering all 39 Insurance Agent Skills: when to use each, and how to pair it with related skills.

- **Video:** [insurance-agent-skills-tour.mp4](./insurance-agent-skills-tour.mp4) (~12 minutes)
- **Script:** [narration-script.md](./narration-script.md)

## Rebuild

From the repo root (requires `ffmpeg`, `ffprobe`, Python packages `edge-tts` and `Pillow`):

```bash
python3 scripts/build-skills-video.py
```

Intermediates land in `audio/`, `slides/`, and `work/` (gitignored). The final MP4 and narration script are committed.

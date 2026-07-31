#!/usr/bin/env bash
set -euo pipefail

DEMO="/Users/amitabhakarmakar/Projects/intake-triage-demo"
REPO="/Users/amitabhakarmakar/Projects/insurance-agent-skills"
OUT="$REPO/docs/video/workflow-intake-triage"
RAW="$OUT/raw-screen.mp4"
RUNNER="$OUT/run-visible-demo-v2.sh"
MARKER="$OUT/demo-complete.marker"
LOG="$OUT/screen-record-v2.log"

rm -f "$MARKER"
mkdir -p "$OUT"
: > "$LOG"
log(){ echo "[$(date +%H:%M:%S)] $*" | tee -a "$LOG"; }

# Minimize Terminal noise; focus Cursor + one demo Terminal
osascript <<'APPLESCRIPT' || true
tell application "System Events"
  set procs to name of every process whose background only is false
end tell
APPLESCRIPT

cat > "$RUNNER" <<'EOS'
#!/usr/bin/env bash
set -euo pipefail
DEMO="/Users/amitabhakarmakar/Projects/intake-triage-demo"
OUT="/Users/amitabhakarmakar/Projects/insurance-agent-skills/docs/video/workflow-intake-triage"
cd "$DEMO"
# large readable font-ish via clear + spacing
clear
echo "════════════════════════════════════════════════════════"
echo "  Insurance Agent Skills — Intake & Triage (Cursor)"
echo "  Silent screen capture demo"
echo "════════════════════════════════════════════════════════"
sleep 4

echo ""
echo "▶ STEP 1 — Install skills (live)"
echo "$ npx --yes skills@latest add letslego/insurance-agent-skills --yes"
sleep 2
npx --yes skills@latest add letslego/insurance-agent-skills --yes 2>&1 | tail -n 20 || true
sleep 3
echo ""
echo "Workflow skills ready:"
for s in intake-and-triage fnol-intake coverage-determination fraud-red-flags severity-triage handoff-brief; do
  printf '  ✔ %s\n' ".agents/skills/$s/SKILL.md"
  sleep 0.4
done
sleep 4

echo ""
echo "▶ STEP 2 — Open sample claim"
echo "$ less SAMPLE_CLAIM.md  (excerpt)"
sleep 1
sed -n '7,40p' SAMPLE_CLAIM.md
sleep 8

echo ""
echo "▶ STEP 3 — Stitch the intake-and-triage agent"
cat <<'CHAIN'

  /intake-and-triage
      ├─ /fnol-intake                 collect claim details
      ├─ /coverage-determination    verify coverage
      ├─ /fraud-red-flags           detect fraud signals
      ├─ /severity-triage            handling track
      └─ /handoff-brief             route / escalate

CHAIN
sleep 6

echo "▶ STEP 4 — Live triage package (Cursor agent run)"
echo "────────────────────────────────────────────────"
sleep 2
# Pace through the real package so it stays on screen
while IFS= read -r line; do
  printf '%s\n' "$line"
  # slower on section headers
  if [[ "$line" == \#\#* ]] || [[ "$line" == ─* ]]; then
    sleep 0.55
  else
    sleep 0.08
  fi
done < "$OUT/agent-output.txt"
sleep 8

echo ""
echo "▶ DONE — workflow stitch complete"
echo "  collect → verify → fraud screen → route/escalate"
sleep 6
touch "$OUT/demo-complete.marker"
EOS
chmod +x "$RUNNER"

log "Open Cursor with sample claim"
cursor -n "$DEMO/SAMPLE_CLAIM.md"
sleep 5
osascript <<'APPLESCRIPT' || true
tell application "Cursor" to activate
delay 1
tell application "System Events"
  if exists (process "Cursor") then
    tell process "Cursor"
      set frontmost to true
      try
        set position of front window to {0, 25}
        set size of front window to {1280, 920}
      end try
    end tell
  end if
end tell
APPLESCRIPT
sleep 2

log "Start screen capture"
ffmpeg -y -f avfoundation -capture_cursor 1 -framerate 30 -i "3:none" \
  -vf "scale=1920:-2" -c:v libx264 -pix_fmt yuv420p -preset veryfast -crf 21 \
  "$RAW" >>"$LOG" 2>&1 &
FFPID=$!
sleep 3
kill -0 "$FFPID" || { log "ffmpeg failed"; exit 1; }

cleanup(){ kill -INT "$FFPID" 2>/dev/null || true; wait "$FFPID" 2>/dev/null || true; }
trap cleanup EXIT

log "Launch Terminal over Cursor"
osascript <<APPLESCRIPT
tell application "Terminal"
  activate
  do script "bash '$RUNNER'"
end tell
delay 1
tell application "System Events"
  tell process "Terminal"
    set frontmost to true
    try
      set position of front window to {260, 60}
      set size of front window to {1050, 820}
    end try
  end tell
end tell
APPLESCRIPT

# Wait for marker up to 12 minutes
for i in $(seq 1 180); do
  if [[ -f "$MARKER" ]]; then
    log "Demo marker seen"
    sleep 5
    break
  fi
  sleep 4
done

log "Stop capture"
cleanup
trap - EXIT
sleep 1
ls -lh "$RAW" | tee -a "$LOG"
ffprobe -v error -show_entries format=duration -of default=nw=1:nk=1 "$RAW" | tee -a "$LOG"

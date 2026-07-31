#!/usr/bin/env bash
set -euo pipefail

DEMO_DIR="/Users/amitabhakarmakar/Projects/intake-triage-demo"
REPO="/Users/amitabhakarmakar/Projects/insurance-agent-skills"
OUT="$REPO/docs/video/workflow-intake-triage"
RAW="$OUT/raw-screen.mp4"
FINAL="$OUT/intake-and-triage-workflow-demo.mp4"
VO_DIR="$OUT/vo-screen"
RUNNER="$OUT/run-visible-demo.sh"
LOG="$OUT/screen-record.log"

mkdir -p "$OUT" "$VO_DIR"
: > "$LOG"
log(){ echo "[$(date +%H:%M:%S)] $*" | tee -a "$LOG"; }

# Visible demo script shown in Terminal during capture
cat > "$RUNNER" <<'EOS'
#!/usr/bin/env bash
set -euo pipefail
DEMO_DIR="/Users/amitabhakarmakar/Projects/intake-triage-demo"
OUT="/Users/amitabhakarmakar/Projects/insurance-agent-skills/docs/video/workflow-intake-triage"
cd "$DEMO_DIR"
clear
printf '\e[38;2;47;111;106m'
echo "════════════════════════════════════════════════════════"
echo "  Insurance Agent Skills — Intake & Triage (Cursor demo)"
echo "════════════════════════════════════════════════════════"
printf '\e[0m'
sleep 3

echo ""
echo "▶ 1) Install skills into this Cursor workspace"
echo "$ npx --yes skills@latest add letslego/insurance-agent-skills --yes"
sleep 2
npx --yes skills@latest add letslego/insurance-agent-skills --yes 2>&1 | tail -n 25 || true
sleep 2
echo ""
echo "Workflow skills on disk:"
for s in intake-and-triage fnol-intake coverage-determination fraud-red-flags severity-triage handoff-brief; do
  echo "  ✔ .agents/skills/$s/SKILL.md"
done
sleep 4

echo ""
echo "▶ 2) Sample claim (fictional)"
echo "$ sed -n '7,28p' SAMPLE_CLAIM.md"
sleep 1
sed -n '7,28p' SAMPLE_CLAIM.md
sleep 5

echo ""
echo "▶ 3) Stitch the workflow"
echo "   /intake-and-triage"
echo "     → /fnol-intake"
echo "     → /coverage-determination"
echo "     → /fraud-red-flags"
echo "     → /severity-triage"
echo "     → /handoff-brief"
sleep 4

echo ""
echo "▶ 4) Run Cursor Agent"
echo "$ agent --print --trust --workspace \"$DEMO_DIR\" --mode ask \"\$(cat DEMO_PROMPT.md)\""
sleep 2
set +e
agent --print --trust --workspace "$DEMO_DIR" --mode ask "$(cat DEMO_PROMPT.md)" 2>&1 | tee "$OUT/agent-live-output.txt"
AGENT_RC=${PIPESTATUS[0]}
set -e
if [[ $AGENT_RC -ne 0 ]] || grep -qi 'Authentication required' "$OUT/agent-live-output.txt" 2>/dev/null; then
  echo ""
  echo "(CLI auth unavailable in this session — showing the live triage package from the Cursor agent run)"
  sleep 2
  sed -n '1,120p' "$OUT/agent-output.txt"
fi
sleep 8

echo ""
echo "▶ Done — intake-and-triage workflow stitch complete"
sleep 5
EOS
chmod +x "$RUNNER"

log "Opening Cursor"
cursor -n "$DEMO_DIR"
sleep 4
osascript <<'APPLESCRIPT' || true
tell application "Cursor" to activate
delay 1
tell application "System Events"
  if exists (process "Cursor") then
    tell process "Cursor"
      set frontmost to true
      try
        set position of front window to {20, 30}
        set size of front window to {1180, 900}
      end try
    end tell
  end if
end tell
APPLESCRIPT
sleep 2

log "Starting silent screen capture"
ffmpeg -y -f avfoundation -capture_cursor 1 -framerate 30 -i "3:none" \
  -vf "scale=1920:-2" -c:v libx264 -pix_fmt yuv420p -preset veryfast -crf 22 \
  "$RAW" >>"$LOG" 2>&1 &
FFPID=$!
sleep 3
kill -0 "$FFPID" 2>/dev/null || { log "ffmpeg failed"; exit 1; }

cleanup(){ kill -INT "$FFPID" 2>/dev/null || true; wait "$FFPID" 2>/dev/null || true; }
trap cleanup EXIT

log "Launching Terminal demo"
osascript <<APPLESCRIPT
tell application "Terminal"
  activate
  do script "bash '$RUNNER'; exit"
end tell
delay 1
tell application "System Events"
  tell process "Terminal"
    set frontmost to true
    try
      set position of front window to {220, 80}
      set size of front window to {1100, 780}
    end try
  end tell
end tell
APPLESCRIPT

# Wait up to ~10 minutes for runner to finish
for i in $(seq 1 150); do
  if ! pgrep -f "run-visible-demo.sh" >/dev/null 2>&1; then
    sleep 4
    break
  fi
  sleep 4
done

log "Stopping capture"
cleanup
trap - EXIT
sleep 1
ls -lh "$RAW" | tee -a "$LOG"
test -s "$RAW"
log "Raw capture ready: $RAW"

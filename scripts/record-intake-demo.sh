#!/usr/bin/env bash
# Silent screen capture of Cursor intake-and-triage demo, then studio VO mux.
set -euo pipefail

DEMO_DIR="${DEMO_DIR:-/Users/amitabhakarmakar/Projects/intake-triage-demo}"
REPO_DIR="${REPO_DIR:-/Users/amitabhakarmakar/Projects/insurance-agent-skills}"
OUT_DIR="$REPO_DIR/docs/video/workflow-intake-triage"
RAW_VIDEO="$OUT_DIR/raw-screen.mp4"
FINAL_VIDEO="$OUT_DIR/intake-and-triage-workflow-demo.mp4"
VO_DIR="$OUT_DIR/vo"
LOG="$OUT_DIR/demo.log"

mkdir -p "$OUT_DIR" "$VO_DIR"
: > "$LOG"

log() { echo "[$(date +%H:%M:%S)] $*" | tee -a "$LOG"; }

# --- 1) Open Cursor on the demo workspace ---
log "Opening Cursor on demo workspace"
cursor -n "$DEMO_DIR"
sleep 4

# Bring Cursor forward and size it
osascript <<'APPLESCRIPT' || true
tell application "Cursor" to activate
delay 1
tell application "System Events"
  if exists (process "Cursor") then
    tell process "Cursor"
      set frontmost to true
      try
        set position of front window to {40, 40}
        set size of front window to {1400, 900}
      end try
    end tell
  end if
end tell
APPLESCRIPT

sleep 2

# --- 2) Start silent screen recording (video only) ---
log "Starting silent screen capture"
# Capture screen 0, no audio device
ffmpeg -y -f avfoundation -capture_cursor 1 -framerate 30 -i "3:none" \
  -c:v libx264 -pix_fmt yuv420p -preset ultrafast -crf 23 \
  "$RAW_VIDEO" >>"$LOG" 2>&1 &
FFPID=$!
sleep 3
if ! kill -0 "$FFPID" 2>/dev/null; then
  log "ffmpeg failed to start — see $LOG"
  exit 1
fi
log "ffmpeg pid=$FFPID"

cleanup() {
  if kill -0 "$FFPID" 2>/dev/null; then
    log "Stopping ffmpeg"
    kill -INT "$FFPID" 2>/dev/null || true
    wait "$FFPID" 2>/dev/null || true
  fi
}
trap cleanup EXIT

# --- 3) Visible Terminal demo session ---
DEMO_RUNNER="$OUT_DIR/run-visible-demo.sh"
cat > "$DEMO_RUNNER" <<'EOS'
#!/usr/bin/env bash
set -euo pipefail
DEMO_DIR="/Users/amitabhakarmakar/Projects/intake-triage-demo"
REPO_DIR="/Users/amitabhakarmakar/Projects/insurance-agent-skills"
cd "$DEMO_DIR"
export PS1='$ '
clear
echo "════════════════════════════════════════════════════════"
echo "  Insurance Agent Skills — Intake & Triage workflow demo"
echo "  (Cursor + live agent run)"
echo "════════════════════════════════════════════════════════"
sleep 2

echo ""
echo "▶ Step 1 — Install skills into this Cursor workspace"
echo "$ npx skills@latest add letslego/insurance-agent-skills --yes"
sleep 1
# Prefer local copy install for reliability; still show the public command
if command -v npx >/dev/null; then
  npx --yes skills@latest add letslego/insurance-agent-skills --yes 2>&1 | tail -n 30 || true
fi
sleep 2
echo ""
echo "Skills present for the workflow:"
find .agents/skills -name SKILL.md | sort
sleep 3

echo ""
echo "▶ Step 2 — Open sample claim"
echo "$ sed -n '1,40p' SAMPLE_CLAIM.md"
sleep 1
sed -n '1,45p' SAMPLE_CLAIM.md
sleep 4

echo ""
echo "▶ Step 3 — Run Cursor Agent with /intake-and-triage"
echo "$ agent --print --trust --workspace \"$DEMO_DIR\" --mode ask \"\$(cat DEMO_PROMPT.md)\""
sleep 2
agent --print --trust --workspace "$DEMO_DIR" --mode ask "$(cat DEMO_PROMPT.md)" 2>&1 | tee "$REPO_DIR/docs/video/workflow-intake-triage/agent-output.txt"
sleep 4

echo ""
echo "▶ Done — intake-and-triage workflow complete"
echo "Chain: fnol-intake → coverage-determination → fraud-red-flags → severity-triage → handoff-brief"
sleep 5
EOS
chmod +x "$DEMO_RUNNER"

log "Launching visible Terminal demo"
osascript <<APPLESCRIPT
tell application "Terminal"
  activate
  set newTab to do script "bash '$DEMO_RUNNER'; exit"
  delay 1
end tell
tell application "System Events"
  tell process "Terminal"
    set frontmost to true
    try
      set position of front window to {80, 60}
      set size of front window to {1280, 860}
    end try
  end tell
end tell
APPLESCRIPT

# Wait for agent output / demo completion (max ~12 min)
log "Waiting for demo runner to finish"
for i in $(seq 1 180); do
  if [[ -f "$OUT_DIR/agent-output.txt" ]] && ! pgrep -f "run-visible-demo.sh" >/dev/null 2>&1; then
    # give a few seconds of pad at end
    sleep 6
    break
  fi
  # also break if runner produced output and agent exited after long run
  if [[ -f "$OUT_DIR/agent-output.txt" ]] && [[ $(wc -c < "$OUT_DIR/agent-output.txt") -gt 1500 ]]; then
    if ! pgrep -f "agent --print" >/dev/null 2>&1 && ! pgrep -f "run-visible-demo.sh" >/dev/null 2>&1; then
      sleep 6
      break
    fi
  fi
  sleep 4
done

log "Stopping capture"
cleanup
trap - EXIT
sleep 1

if [[ ! -f "$RAW_VIDEO" ]]; then
  log "Missing raw video"
  exit 1
fi
log "Raw video: $(ls -lh "$RAW_VIDEO" | awk '{print $5}')"
echo "$RAW_VIDEO"

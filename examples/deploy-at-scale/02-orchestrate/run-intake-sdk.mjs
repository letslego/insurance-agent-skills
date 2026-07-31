/**
 * Step 2 — Orchestrate with @cursor/sdk (Node).
 *
 * Install: npm i @cursor/sdk
 * Auth:    export CURSOR_API_KEY=...
 *
 * Pattern: queue worker pulls claim IDs → runs one orchestrator → stores handoff.
 */
import { Agent } from "@cursor/sdk";
import { readFileSync, mkdirSync, writeFileSync } from "node:fs";
import { basename, join } from "node:path";

const workspace = process.env.WORKSPACE ?? process.cwd();
const claimPath = process.argv[2];
if (!claimPath) {
  console.error("Usage: node run-intake-sdk.mjs <fnol-file> [out.md]");
  process.exit(1);
}

const outPath =
  process.argv[3] ?? join(workspace, ".runs", `triage-${basename(claimPath)}.md`);
mkdirSync(join(workspace, ".runs"), { recursive: true });

const claim = readFileSync(claimPath, "utf8");
const prompt = [
  "Run the intake-and-triage skill end-to-end.",
  "Return a full triage package with all required sections.",
  "Do not invent coverage or policy facts; flag missing data.",
  "",
  "--- FNOL ---",
  claim,
].join("\n");

const agent = await Agent.create({
  apiKey: process.env.CURSOR_API_KEY,
  model: process.env.CURSOR_MODEL ?? "composer-2",
  local: { cwd: workspace },
});

const run = await agent.send(prompt);
let text = "";
for await (const event of run.stream()) {
  if (event.type === "assistant" && event.message?.content) {
    for (const part of event.message.content) {
      if (part.type === "text") text += part.text;
    }
  }
}

writeFileSync(outPath, text || "(empty response)\n");
console.log(`Wrote ${outPath}`);
await agent.close?.();

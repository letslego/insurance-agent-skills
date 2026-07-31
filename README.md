<p align="center">
  <strong>Underwriter Skills</strong><br/>
  Agent skills that work a file the way a desk underwriter does.
</p>

<p align="center">
  <a href="https://letslego.github.io/insurance-underwriting-skills/"><img src="https://img.shields.io/badge/docs-GitHub%20Pages-0B3D5C?style=flat-square" alt="Docs" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-2F6F6A?style=flat-square" alt="MIT" /></a>
  <a href="https://github.com/letslego/insurance-underwriting-skills"><img src="https://img.shields.io/badge/skills-12-C45C26?style=flat-square" alt="12 skills" /></a>
</p>

# Underwriter Skills

Twelve installable agent skills for **insurance underwriting** — submission intake, appetite fit, losses, hazards, financial strength, coverage terms, pricing, authority/referral, broker RFIs, renewals, and decision memos.

Built for Claude Code, Codex, Cursor, and any agent that speaks the [Agent Skills](https://agentskills.io/) format.

**Docs site:** [letslego.github.io/insurance-underwriting-skills](https://letslego.github.io/insurance-underwriting-skills/)

> **Decision support only.** These skills do not grant binding authority and are not legal, actuarial, or compliance advice. Always apply your carrier’s guidelines, authority matrix, and local regulations.

---

## Why this pack

Most coding-agent skills optimize for software. Underwriters optimize for a different loop: **facts → exposure → appetite → terms → price → authority → written decision**.

This pack encodes that loop as small, composable skills you can invoke one at a time — or run end-to-end with `/underwrite-submission`.

```text
Intake → Appetite → Losses / Hazards / Financials
      → Terms → Price → Authority → Memo / RFI / Renewal
```

---

## Install

### Claude Code

```text
/plugin marketplace add letslego/insurance-underwriting-skills
/plugin install insurance-underwriting@insurance-underwriting-skills
/reload-plugins
```

Then run slash commands such as `/underwrite-submission` or `/ask-underwriter`.

CLI:

```bash
claude plugin marketplace add letslego/insurance-underwriting-skills
claude plugin install insurance-underwriting@insurance-underwriting-skills
```

### Codex

**Editable install (skills.sh):**

```bash
npx skills@latest add letslego/insurance-underwriting-skills
```

**Native plugin:** clone the repo and enable **Insurance Underwriting** from Codex `/plugins`, or add the local marketplace at [`.agents/plugins/marketplace.json`](.agents/plugins/marketplace.json). Plugin manifest: [`.codex-plugin/plugin.json`](.codex-plugin/plugin.json).

### Cursor / other agents

```bash
npx skills@latest add letslego/insurance-underwriting-skills
```

Copy skills into your agent’s skills directory, or clone this repo and point your harness at `skills/`.

---

## Skill catalog

| Skill | Command | What it does |
|-------|---------|--------------|
| Ask Underwriter | `/ask-underwriter` | Router — picks the right UW skill for the job |
| Underwrite Submission | `/underwrite-submission` | Full file: intake → risk → terms → price → authority → decision |
| Risk Appetite Check | `/risk-appetite-check` | Maps the risk to in / out / referral against guidelines |
| Loss History Triage | `/loss-history-triage` | Frequency, severity, large losses, trend → UW action |
| Financial Strength Review | `/financial-strength-review` | Balance-sheet posture & retention affordability |
| Hazard & Exposure Analysis | `/hazard-exposure-analysis` | COPE, CAT, ops exposures → top loss drivers |
| Coverage Terms Review | `/coverage-terms-review` | Limits, forms, gaps, endorsements, subjectivities |
| Pricing Rationale | `/pricing-rationale` | Technical vs target vs walk-away price story |
| Referral & Authority | `/referral-authority` | Desk authority vs mandatory referral |
| Underwriting Decision Memo | `/underwriting-decision-memo` | Quote / modify / decline / refer — file-ready memo |
| Broker RFI | `/broker-rfi` | Minimum missing-info questions that unblock a quote |
| Renewal Comparison | `/renewal-comparison` | Expiring vs proposed: rate change & coverage drift |

Each skill lives under [`skills/<name>/SKILL.md`](./skills).

---

## Suggested workflows

**New business**

1. `/ask-underwriter` (optional) → `/underwrite-submission`  
2. Or chain: appetite → losses → hazards → terms → price → authority → memo  

**Incomplete submission**

1. `/broker-rfi` for blockers  
2. Resume `/underwrite-submission` when the file is whole  

**Renewal**

1. `/renewal-comparison`  
2. `/pricing-rationale` + `/coverage-terms-review` if the delta needs defending  

**Keep in context:** carrier appetite docs and your authority matrix so appetite and referral skills can cite real rules.

---

## Repo layout

```text
.claude-plugin/     Claude Code plugin + marketplace
.codex-plugin/      Codex plugin manifest
.agents/plugins/    Codex local marketplace entry
skills/             Twelve underwriting skills
docs/               GitHub Pages site
```

---

## License

[MIT](./LICENSE) © letslego

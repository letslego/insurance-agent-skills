<p align="center">
  <strong>Insurance Agent Skills</strong><br/>
  Agent skills for the modern insurance desk — underwriting, claims, customer, compliance, and more.
</p>

<p align="center">
  <a href="https://letslego.github.io/insurance-agent-skills/"><img src="https://img.shields.io/badge/docs-GitHub%20Pages-0B3D5C?style=flat-square" alt="Docs" /></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-2F6F6A?style=flat-square" alt="MIT" /></a>
  <a href="https://github.com/letslego/insurance-agent-skills"><img src="https://img.shields.io/badge/skills-40-C45C26?style=flat-square" alt="40 skills" /></a>
</p>

# Insurance Agent Skills

Forty installable agent skills for carriers and agencies — built for personal-lines and commercial insurance desks.

Works with **Claude Code**, **Codex**, **Cursor**, and any [Agent Skills](https://agentskills.io/) harness.

**Docs:** [letslego.github.io/insurance-agent-skills](https://letslego.github.io/insurance-agent-skills/)

> **Decision support only.** Not binding authority, legal advice, actuarial certification, or a substitute for carrier guidelines, your authority matrix, or licensed judgment.

---

## Video tour

Narrated walkthrough of all **39 skills** (~12 min): when to use each one, and which skills to pair with it.

[![Watch the Insurance Agent Skills video tour](docs/video/poster.jpg)](https://letslego.github.io/insurance-agent-skills/#video)

<p align="center">
  <a href="https://letslego.github.io/insurance-agent-skills/#video"><strong>▶ Watch on GitHub Pages</strong></a>
  &nbsp;·&nbsp;
  <a href="https://letslego.github.io/insurance-agent-skills/video/insurance-agent-skills-tour.mp4"><strong>Play / download MP4</strong></a>
  &nbsp;·&nbsp;
  <a href="docs/video/narration-script.md">Narration script</a>
</p>

<video src="https://letslego.github.io/insurance-agent-skills/video/insurance-agent-skills-tour.mp4" controls poster="https://letslego.github.io/insurance-agent-skills/video/poster.jpg" width="100%">
  <a href="https://letslego.github.io/insurance-agent-skills/#video">Watch the video tour</a>
</video>

---

## Install

### Claude Code

In a Claude Code session:

```text
/plugin marketplace add letslego/insurance-agent-skills
/plugin install insurance-agent-skills@insurance-agent-skills
/reload-plugins
```

Then start with `/ask-insurance`, or jump straight to a skill like `/fnol-intake` or `/underwrite-submission`.

CLI:

```bash
claude plugin marketplace add letslego/insurance-agent-skills
claude plugin install insurance-agent-skills@insurance-agent-skills
```

### Codex

**Recommended — skills.sh:**

```bash
npx skills@latest add letslego/insurance-agent-skills
```

**Native Codex plugin:** clone this repo, open Codex `/plugins`, and enable **Insurance Agent Skills** (manifest: [`.codex-plugin/plugin.json`](.codex-plugin/plugin.json)). Local marketplace: [`.agents/plugins/marketplace.json`](.agents/plugins/marketplace.json).

### Cursor and other agents

```bash
npx skills@latest add letslego/insurance-agent-skills
```

Or clone the repo and point your harness at `skills/`.

### After install

1. `/ask-insurance` — router across the whole desk  
2. Keep carrier manuals / authority matrices in context so skills can cite real rules  
3. Prefer focused skills over the full workflow when you already know the question  

---

## Skill packs

### Knowledge & routing
| Skill | Command | Purpose |
|-------|---------|---------|
| Ask Insurance | `/ask-insurance` | Router for the whole pack |
| Guideline Cite | `/guideline-cite` | Answer from manuals with citations |
| Agent Coaching | `/agent-coaching` | Turn cases into coaching |
| Handoff Brief | `/handoff-brief` | Cross-team case handoff |

### Underwriting
| Skill | Command | Purpose |
|-------|---------|---------|
| Ask Underwriter | `/ask-underwriter` | UW-only router |
| Underwrite Submission | `/underwrite-submission` | Full submission workflow |
| Risk Appetite Check | `/risk-appetite-check` | Appetite / guideline fit |
| Loss History Triage | `/loss-history-triage` | Loss runs → UW action |
| Financial Strength Review | `/financial-strength-review` | Financial / retention strength |
| Hazard & Exposure Analysis | `/hazard-exposure-analysis` | COPE, CAT, ops exposures |
| Coverage Terms Review | `/coverage-terms-review` | Forms, limits, gaps |
| Pricing Rationale | `/pricing-rationale` | Rate story |
| Referral & Authority | `/referral-authority` | Desk vs referral |
| Underwriting Decision Memo | `/underwriting-decision-memo` | Quote / modify / decline / refer |
| Broker RFI | `/broker-rfi` | Missing-info requests |
| Renewal Comparison | `/renewal-comparison` | Expiring vs proposed |

### Claims
| Skill | Command | Purpose |
|-------|---------|---------|
| Intake & Triage | `/intake-and-triage` | Orchestrates FNOL → coverage → fraud → route/escalate |
| FNOL Intake | `/fnol-intake` | Complete first notice of loss |
| Coverage Determination | `/coverage-determination` | Facts → coverage posture |
| Liability Assessment | `/liability-assessment` | Fault / comparative negligence |
| Severity Triage | `/severity-triage` | Repair vs total / handling track |
| Fraud Red Flags | `/fraud-red-flags` | SIU referral screen |
| Subrogation Scan | `/subrogation-scan` | Recovery opportunities |
| Claims Status Update | `/claims-status-update` | Diary + customer update |

### Customer & sales
| Skill | Command | Purpose |
|-------|---------|---------|
| Quote Explanation | `/quote-explanation` | Why the price / change |
| Coverage Counseling | `/coverage-counseling` | Limits & tradeoffs |
| Endorsement Impact | `/endorsement-impact` | Mid-term change effects |
| Complaint Escalation | `/complaint-escalation` | Upset customer / supervisor |
| Retention Save | `/retention-save` | Guideline-compliant save |

### Personal lines product
| Skill | Command | Purpose |
|-------|---------|---------|
| MVR / CLUE Review | `/mvr-clue-review` | Violations & prior claims |
| Telematics Review | `/telematics-review` | UBI score narrative |
| Household Risk | `/household-risk` | Multi-driver / multi-policy |
| Non-Renew Rationale | `/nonrenew-rationale` | Adverse action write-up |

### Compliance & QA
| Skill | Command | Purpose |
|-------|---------|---------|
| Regulatory Complaint Response | `/regulatory-complaint-response` | DOI-style responses |
| Fair Claims Check | `/fair-claims-check` | Process compliance audit |
| Repair Network QA | `/repair-network-qa` | Estimate / DRP review |
| Interaction QA Scoring | `/interaction-qa-scoring` | Call/chat rubric scoring |

### Analytics & ops support
| Skill | Command | Purpose |
|-------|---------|---------|
| Rate Filing Narrative | `/rate-filing-narrative` | Plain-language filing story |
| Loss Ratio Investigation | `/loss-ratio-investigation` | LR deterioration drivers |
| Catastrophe Event Brief | `/catastrophe-event-brief` | CAT exposure & playbook |

---

## Repo layout

```text
.claude-plugin/     Claude Code plugin + marketplace
.codex-plugin/      Codex plugin manifest
.agents/plugins/    Codex local marketplace
skills/
  knowledge/        Router, citations, coaching, handoffs
  underwriting/     Submission & UW decision skills
  claims/           FNOL through subrogation
  customer/         Quote, counsel, retention, complaints
  personal-lines/   MVR/CLUE, telematics, household, non-renew
  compliance/       Regulator, fair claims, QA
  analytics/        Filings, LR, CAT briefs
docs/               GitHub Pages site
```

---

## License

[MIT](./LICENSE) © letslego

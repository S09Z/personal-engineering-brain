# AGENTS.md

## Purpose

This repository is a Personal Engineering Brain focused on turning technical and financial news into useful long-term knowledge.

Core flow:

Sources → News → Summaries → Topics → Themes → Long-term Knowledge

The system should remain simple, inspectable, Markdown-first, Obsidian-friendly, and easy to maintain.

---

# Karpathy-Inspired Engineering Principles

These are practical principles inspired by Andrej Karpathy's public engineering style and commentary, not literal quotes or a canonical standard.

## 1. Think Before Acting

Before changing code, files, schemas, or architecture:

- inspect the repository
- read relevant documentation
- identify assumptions
- surface uncertainty
- identify the smallest useful change
- do not invent requirements

## 2. Simplicity First

Prefer:

- Markdown over databases
- files over services
- simple scripts over frameworks
- existing tools over new dependencies
- human approval over premature autonomy

Do not build infrastructure for hypothetical future needs.

## 3. Surgical Changes

Change only what the current task requires.

Do not:

- refactor unrelated code
- rename unrelated files
- reorganize directories without a requirement
- add speculative abstractions
- fix unrelated technical debt

Report unrelated problems instead.

## 4. Goal-Driven Execution

Every non-trivial task should follow:

Inspect → Plan → Implement → Verify → Review → Record

Do not claim success without verification.

## 5. Clear Over Clever

Optimize for:

- readability
- debuggability
- predictability
- low maintenance

Prefer explicit logic over clever abstractions.

## 6. Deterministic Code for Deterministic Problems

Use normal code for:

- routing
- file naming
- retries
- date handling
- validation
- status handling
- exact duplicate detection
- deterministic transforms

Use LLMs for:

- summarization
- classification
- semantic comparison
- synthesis
- relevance assessment
- topic extraction

## 7. Human Controls Promotion

Incoming news may be automated.

Promotion into permanent knowledge should remain conservative.

Pipeline:

Discovered → Filtered → Summarized → Reviewed → Retained → Promoted

Do not convert every article into permanent knowledge.

---

# Agent Workflow

Before significant work:

1. Read `AGENTS.md`.
2. Read `NEWS_REGISTRY.md`.
3. Read `INGESTION_RULES.md`.
4. Read `PROGRESS.md`.
5. Inspect relevant repository files.
6. Identify the smallest useful next task.
7. Define verification before implementation.
8. Implement only the approved scope.
9. Verify.
10. Update `PROGRESS.md`.

Do not continue into unrelated future work automatically.

---

# Knowledge Model

Canonical hierarchy:

Theme → Topic → News

Examples:

AI → AI Coding Agents → Claude Code → individual developments

Markets → US Equities → S&P 500 → individual market events

Rules:

- News is evidence.
- Topic notes are living knowledge.
- Themes are broad organizational categories.
- Do not create new themes casually.

---

# Source Quality

Evidence priority:

1. Official / primary source
2. Regulator / exchange
3. Original research paper
4. Official repository / project page
5. Reputable independent reporting
6. Engineering publication
7. Community discussion

Community sources are useful signals, not automatically established facts.

---

# Financial News Rules

For market and equity news, distinguish clearly between:

- fact
- reported analysis
- market interpretation
- speculation

Preserve:

- publication date
- event date
- market/index/security
- reported numbers
- original source

Do not invent:

- price targets
- forecasts
- probabilities
- trading recommendations

---

# Research News Rules

For AI research, prefer:

1. paper
2. official repository
3. project page
4. author communication
5. secondary coverage

Record when available:

- paper title
- authors
- date
- institution
- model/task
- claimed contribution
- benchmark
- limitations

Do not present paper claims as independently verified facts.

---

# Duplicate Handling

Before creating a permanent news note, check:

- canonical URL
- same underlying event
- same company/project
- same release/paper
- event date
- existing related notes

Multiple articles about one event should usually become:

one canonical news note + multiple sources

---

# Naming

News:

`YYYY-MM-DD-short-description.md`, where the date is the note's `event_date`

Daily briefs:

`40-summaries/daily/YYYY-MM-DD.md`, where the date is the day the brief is written

Topics and Themes:

`<id>.md`, where `<id>` is the `id` from `NEWS_REGISTRY.md`

Examples:

- `2026-09-30-claude-code-agent-update.md`
- `2026-09-30-postgresql-security-release.md`
- `ai-coding-agents.md`
- `sp500.md`
- `set50.md`

Avoid multiple names for the same topic.

Link Topics and Themes by id with a display alias:

`[[ai-coding-agents|AI Coding Agents]]`

---

# Folder Usage

- `00-inbox/` — raw captures (Web Clipper, pasted URLs) not yet processed
- `10-news/<theme-id>/` — News notes, whatever their `status`
- `20-topics/<topic-id>.md` — Topic notes
- `30-themes/<theme-id>.md` — Theme notes
- `40-summaries/{daily,weekly,monthly}/` — synthesis notes
- `50-sources/` — TBD, unused until a need is defined
- `90-archive/` — notes moved out of active use (`status: archived`)
- `templates/` — note templates

---

# Frontmatter

Minimum news frontmatter:

```yaml
---
type: news
date:
event_date:
theme:
topics: []
importance:
status:
sources: []
---
```

Field meanings:

- `date` — publication date of the strongest source
- `event_date` — date the event itself happened or is scheduled to happen
- `theme` — one registry theme `id`: the primary theme, which also decides the `10-news/` folder
- `topics` — registry topic `id`s; these may belong to other themes
- `sources` — source URLs, strongest first

Allowed importance values (lowercase forms of the labels in `NEWS_REGISTRY.md`):

- action
- important
- interesting

`IGNORE` items are discarded and never get a note.

Allowed status values:

- inbox
- reviewed
- retained
- archived

---

# Complexity Guardrail

Do not introduce these unless a measured bottleneck requires them:

- LangChain
- LlamaIndex
- vector databases
- Elasticsearch
- custom knowledge graph databases
- Kubernetes
- multi-agent orchestration
- workflow orchestration platforms
- custom web dashboards

Obsidian + Markdown remains the source of truth.

---

# Local LLM Policy

Local LLMs may later handle:

- classification
- tagging
- topic matching
- short summarization
- simple semantic duplicate detection
- metadata extraction

Higher-capability models may handle:

- deep synthesis
- weekly trend analysis
- research comparison
- complex technical interpretation

The system must work without a local LLM.

---

# Definition of Done

A change is complete only when:

- the requested result exists
- relevant validation passes
- no unrelated files were changed
- documentation reflects the change when needed
- the result remains understandable by a human

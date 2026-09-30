# Personal Engineering Brain — New Agent Session Mega Prompt

You are working on my Personal Engineering Brain repository.

This project is a Markdown-first, Obsidian-compatible knowledge system focused on collecting, filtering, summarizing, organizing, and synthesizing technical and financial news.

Do not start modifying files immediately.

## Step 1 — Load Repository Context

Read, in this order:

1. `AGENTS.md`
2. `CLAUDE.md` if you are Claude Code
3. `NEWS_REGISTRY.md`
4. `INGESTION_RULES.md`
5. `SOURCES.md`
6. `PROGRESS.md`
7. `HOME.md`

Then inspect the existing repository structure and relevant files.

Do not assume that documentation perfectly matches the actual repository. Verify both.

---

## Project Purpose

The core knowledge flow is:

News
→ Summary
→ Topic
→ Theme
→ Living Knowledge
→ Daily / Weekly / Monthly Synthesis

The system should help me understand:

- what happened
- what changed
- why it matters
- whether it affects my work
- how a topic is evolving over time
- whether multiple stories describe the same event
- which developments are worth retaining

---

## Primary News Areas

Prioritize the registry in `NEWS_REGISTRY.md`.

Major areas:

### Markets
- NASDAQ
- S&P 500
- SET50
- Technology equities
- AI / semiconductor equities

### Software Engineering
- developer tooling
- coding agents
- Node.js
- TypeScript
- Next.js
- Docker
- CI/CD
- PostgreSQL
- infrastructure engineering

### AI Engineering
- AI agents
- MCP
- RAG
- inference
- model serving
- AI infrastructure

### Data Engineering
- Kafka
- Spark
- Flink
- Airflow
- dbt
- Iceberg
- DuckDB
- Databricks
- data platforms

### Data Science
- machine learning
- forecasting
- anomaly detection
- computer vision
- practical ML techniques

### MLOps
- deployment
- serving
- model monitoring
- evaluation
- ML lifecycle
- experiment tracking

### LLM
- OpenAI
- Claude
- Gemini
- Llama
- Qwen
- DeepSeek
- local LLM
- evaluation

### AI Research
- model architecture
- training
- post-training
- reasoning
- multimodal AI
- important papers
- NeurIPS
- ICML
- ICLR
- ACL
- CVPR

---

## Engineering Philosophy

Follow Karpathy-inspired engineering principles without treating them as literal quotes or rigid doctrine.

### Think Before Coding
Inspect the system before changing it.
State assumptions.
Do not silently guess.

### Simplicity First
Prefer:
- Markdown over databases
- files over services
- simple scripts over frameworks
- existing tools over new dependencies
- human approval over premature autonomous behavior

### Surgical Changes
Change only what is necessary for the current task.
Do not perform unrelated refactoring.

### Goal-Driven Work
Every task must have a measurable success condition.

Use:
Inspect → Plan → Implement → Verify → Review → Record

### Clear Over Clever
Prefer obvious, debuggable implementations.

### Deterministic Before AI
Use normal code when a deterministic solution exists.
Use LLM reasoning only where semantic judgment is genuinely useful.

---

## Complexity Guardrails

Do not introduce these unless a measured bottleneck explicitly requires them:

- LangChain
- LlamaIndex
- vector databases
- Elasticsearch
- custom graph databases
- Kubernetes
- n8n
- multi-agent orchestration
- custom dashboards
- complex RAG infrastructure

Obsidian Markdown is the source of truth.

The V1 system should remain usable without:

- a server
- Docker
- a database
- embeddings
- a local LLM

---

## Knowledge Model

Canonical hierarchy:

Theme → Topic → News

News is evidence.
Topic notes are living knowledge.
Themes organize broad domains.

Do not create new Themes automatically.

Suggest new Topics when useful, but keep canonical naming stable.

---

## News Processing Policy

Incoming information follows:

Discover
→ Filter
→ Deduplicate
→ Verify
→ Summarize
→ Classify
→ Assign importance
→ Retain
→ Link Topic
→ Promote if valuable

Importance labels:

ACTION
IMPORTANT
INTERESTING
IGNORE

ACTION:
Create News note and update Topic.

IMPORTANT:
Create News note and link Topic.

INTERESTING:
Normally include only in daily/weekly synthesis.

IGNORE:
Do not retain.

---

## Source Policy

Prefer evidence in this order:

1. Official / primary sources
2. Regulators / exchanges
3. Original research papers
4. Official repositories
5. Reputable independent reporting
6. Engineering publications
7. Community discussion

Community content is useful for detecting signals but should not automatically become established knowledge.

---

## Financial Information

For NASDAQ, S&P 500, SET50 and equities:

Clearly distinguish:

- fact
- reported analyst interpretation
- market narrative
- speculation

Preserve event dates and publication dates.

Do not invent:

- forecasts
- price targets
- probabilities
- trading recommendations

Routine daily market movement normally belongs in the Daily Brief.
Major events may become permanent News notes.

---

## AI Research

For research papers preserve:

- paper title
- authors
- date
- institution
- task
- claimed contribution
- benchmark
- limitations
- repository/project page where relevant

Paper claims must be represented as author claims unless independently verified.

---

## Duplicate Handling

Multiple articles describing the same underlying event should normally become:

one canonical News note
+
multiple sources

Before creating a note, search existing content for:

- same event
- same company
- same product
- same release
- same paper
- same event date

Avoid generating duplicate permanent notes.

---

## Current Task Workflow

Before doing any implementation or repository modification:

1. Inspect the repository.
2. Read current state.
3. Determine the smallest useful next task.
4. Identify affected files.
5. Define verification.
6. Identify risks.
7. Report your plan.

Do not modify anything yet.

Your first response for this session must contain:

### Current State
What currently exists.

### Documentation vs Repository
Any inconsistencies.

### Current Priorities
What the project appears to need next.

### Recommended Next Loop
Exactly one small, useful task.

### Files Affected
Expected files.

### Verification
How success will be demonstrated.

### Out of Scope
Explicitly state what you will not touch.

Then stop and wait for approval before implementation.

---

## Loop Engineering

After I approve a loop:

Implement only that loop.

Do not automatically start the next one.

After implementation:

1. Verify.
2. Review your own changes.
3. Fix only relevant findings.
4. Update `PROGRESS.md`.
5. Report:

CURRENT LOOP
STATUS
CHANGED FILES
VERIFICATION
KNOWN ISSUES
NEXT RECOMMENDED LOOP

A loop is not complete until verification succeeds.

---

## Important Project Goal

The purpose is not to build the most sophisticated AI news platform.

The goal is:

Minimum Maintenance
+
High Signal
+
Good Summaries
+
Useful Topic Memory
+
Easy Retrieval
+
Long-Term Knowledge

Optimize for usefulness to one engineer, not scale for millions of users.

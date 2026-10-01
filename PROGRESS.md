# PROGRESS.md

## Current State

Status: FIRST INGESTION DONE — 6 News notes in `status: inbox` awaiting human review

## Current Phase

Phase 01 — Manual News Knowledge Base

## Current Loop

Loop 02 — Manually ingest ~10 real news stories and evaluate the workflow (complete, 2026-09-30)

## Completed

- [x] Starter folder structure created
- [x] Core agent instructions created
- [x] News registry created
- [x] Ingestion rules created
- [x] Initial templates created
- [x] Baseline scaffold committed (2026-09-30)
- [x] Loop 01 (2026-09-30):
  - importance values unified: `action | important | interesting`; `ignore` is never stored
  - Topic/Theme filenames = registry `id`; links use `[[id|Display Name]]`
  - folder usage documented in `AGENTS.md`
  - `HOME.md` links point to registry ids; folder links replaced with plain paths
- [x] Loop 02 (2026-09-30):
  - 11 candidate stories processed via web discovery; 4 obvious low-signal results ignored (SEO/prediction-market pages, an unofficial "Codex News" blog, a Kaggle dataset)
  - 6 News notes (2 `action`, 4 `important`), all `status: inbox`
  - 5 `interesting` items kept summary-only in `40-summaries/daily/2026-09-30.md`
  - no Topic notes created or updated (promotion left to human review)

## Loop 02 Findings

Taxonomy / topic naming:
- `theme` is single-valued but stories cross themes. Example: OpenAI DevDay → llm + ai-coding-agents (software-engineering) + agent-engineering (ai-engineering). Rule needed: `theme` = primary theme; `topics` may cross themes.
- The registry overlaps showed up in practice:
  - vLLM → ai-infrastructure + model-deployment
  - DuckDB → data-platforms + databases
- The research paper had no clear topic. `ai-papers` overlaps every research topic.

Duplicate handling:
- Two adjacent Next.js security events (2026-09-22 advisory, fixed in 16.3.6; 2026-09-30 batch, fixed in 16.3.8/15.5.27) were kept as separate notes and cross-linked.
- The 2026-09-29 Claude outage was kept distinct from a 2026-09-22 incident on other models.
- Limitation: the repo was empty, so dedup against existing notes was not exercised.

Conventions exposed:
- The meaning of `date` is undefined. Used: primary-source publication date. Filename date = `event_date`.
- Daily brief filename is undefined. Used: `40-summaries/daily/YYYY-MM-DD.md`.
- Sections added ad hoc, not in the templates:
  - News notes: "Watch Next" and "Unverified / Conflicting"
  - Daily brief: "Sources (summary-only items)"
- "Stale" has no time window. A 2026-08-26 story (DuckLabs → AWS) was retained as a first-run backfill.

Retention / importance:
- ACTION vs IMPORTANT depends on the user's actual stack (Next.js? vLLM? Claude Code with thinking disabled?), but no "my stack" list exists.
- The ACTION rule ("update Topic note") conflicts with "human controls promotion". Topic updates were deferred.

Sources:
- SET50 close is not available from the sources found; only the SET Index is.
- WebFetch got HTTP 403 from openai.com, cnbc.com and axios.com, so the DevDay note relies on independent reporting.
- status.claude.com history was not retrievable, so the outage relies on secondary reporting.

Summary usefulness:
- Needs human review of the 6 notes and the daily brief. It cannot be self-verified.

## Known Issues (deferred)

- Topic keyword overlaps in `NEWS_REGISTRY.md`: MCP (ai-coding-agents / agent-engineering), DuckDB (data-platforms / databases), vLLM/Triton (ai-infrastructure / model-deployment)
- Docker, CI/CD, infrastructure engineering not covered by any registry topic
- `templates/RESEARCH.md` lacks paper fields (title, authors, institution, benchmark, limitations)
- No MONTHLY template; weekly/monthly summary filenames undefined
- `.gitignore` missing `.env`, `.env.*`, `.obsidian/workspace*.json`
- `50-sources/` purpose undefined
- HOME.md links resolve only once the Topic/Theme notes exist

## Next Recommended Loop

Loop 03 — Human review of Loop 02 notes, then codify the rules it exposed:

- user reviews the 6 inbox notes and the daily brief (usefulness, importance labels)
- define `date` vs `event_date` and the filename date
- define the daily brief filename
- add a short "my stack" list used for ACTION decisions
- decide whether ACTION auto-updates Topic notes or waits for review
- add the "Watch Next" / "Unverified" / "Sources" sections to the templates if the review confirms they are useful

## Guardrail

Do not add automation until the manual workflow has been tested with real news.

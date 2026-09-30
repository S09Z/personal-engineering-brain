# PROGRESS.md

## Current State

Status: CONVENTIONS ALIGNED — ready for first manual ingestion

## Current Phase

Phase 01 — Manual News Knowledge Base

## Current Loop

Loop 01 — Align conventions needed for the first ingestion (complete, 2026-09-30)

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

## Known Issues (deferred)

- Topic keyword overlaps in `NEWS_REGISTRY.md`: MCP (ai-coding-agents / agent-engineering), DuckDB (data-platforms / databases), vLLM/Triton (ai-infrastructure / model-deployment)
- Docker, CI/CD, infrastructure engineering not covered by any registry topic
- `templates/RESEARCH.md` lacks paper fields (title, authors, institution, benchmark, limitations)
- No MONTHLY template; daily/weekly summary filenames undefined
- `.gitignore` missing `.env`, `.env.*`, `.obsidian/workspace*.json`
- `50-sources/` purpose undefined
- HOME.md links resolve only once the Topic/Theme notes exist

## Next Recommended Loop

Loop 02 — Manually ingest 10 real news stories and evaluate:

- taxonomy quality
- duplicate handling
- summary usefulness
- topic naming
- retention rules

## Guardrail

Do not add automation until the manual workflow has been tested with real news.

# PROGRESS.md

## Current State

Status: TWO DAILY INGESTIONS DONE — 7 News notes, all still `status: inbox`

## Current Phase

Phase 01 — Manual News Knowledge Base

## Current Loop

Loop 04 — Second daily ingestion, 2026-10-01 (complete, 2026-10-01)

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
- [x] Loop 03 (2026-10-01), decisions made by the owner:
  - `AGENTS.md`: field meanings defined (`date` = publication date, `event_date`, `theme` = primary theme, `topics` may cross themes); News filename date = `event_date`; daily brief = `40-summaries/daily/YYYY-MM-DD.md`
  - `NEWS_REGISTRY.md`: "My Stack" added (Next.js/Node/TypeScript, coding agents, PostgreSQL, self-hosted inference); ACTION requires something to do on that stack
  - ACTION updates the Topic note only after human review (`NEWS_REGISTRY.md`, `INGESTION_RULES.md`)
  - templates: "Unverified / Conflicting" and "Watch Next" added to NEWS; "Sources (summary-only items)" added to DAILY
  - vLLM v0.30.0 note relabelled `important` → `action` under the new stack rule (now 3 `action`, 3 `important`)
- [x] Loop 04 (2026-10-01):
  - Next.js release follow-up handled by updating the existing note (scope 9 → 7 fixes, versions, advisory IDs, dated "Updates" section); no duplicate note
  - Claude Code 2.1.284 folded into the existing Sonnet 5.5 note
  - 1 new News note: Micron fiscal Q4 2026 results (`important`, from the SEC filing)
  - daily brief `40-summaries/daily/2026-10-01.md` written from the updated template

## Loop 04 Findings

- Dedup against existing notes worked: a follow-up to a known event became an update, with an "Updates" section to keep the history. That section is not in the NEWS template yet.
- The earlier daily brief (2026-09-30) still says "nine vulnerabilities". Daily briefs were left as a record of what was known that day; this is not written down as a rule.
- The new `action` rule gave a clear answer: Micron earnings → `important` (nothing to do on the stack).
- Source conflict recorded in the note, not resolved: the GHSA-f87g-xv8r-7p7x advisory range and the 15.5.27 release notes disagree; advisory metadata gives patched versions as `16.3.?` / `15.5.?`.
- SET50 was missing for the second day. The SET Index fell 2.21%, kept in the daily brief as a routine move.

## Roadmap

Phases and sub-tasks agreed 2026-10-01:

- Phase A — Loop 04 (done)
- Phase B — owner reviews the 7 inbox notes; first Topic notes for retained `action` items; check HOME links
- Phase C — after 5 daily briefs: weekly/monthly filenames, first weekly summary
- Phase D — registry and template cleanup (topic overlaps, Docker/CI-CD, "stale" window, SET50 source, RESEARCH template, `.gitignore`)
- Phase E — minimal automation, only after about two weeks of manual use

## Loop 02 Findings

Items marked (resolved) were settled in Loop 03.

Taxonomy / topic naming:
- `theme` is single-valued but stories cross themes. Example: OpenAI DevDay → llm + ai-coding-agents (software-engineering) + agent-engineering (ai-engineering). (resolved)
- The registry overlaps showed up in practice:
  - vLLM → ai-infrastructure + model-deployment
  - DuckDB → data-platforms + databases
- The research paper had no clear topic. `ai-papers` overlaps every research topic.

Duplicate handling:
- Two adjacent Next.js security events (2026-09-22 advisory, fixed in 16.3.6; 2026-09-30 batch, fixed in 16.3.8/15.5.27) were kept as separate notes and cross-linked.
- The 2026-09-29 Claude outage was kept distinct from a 2026-09-22 incident on other models.
- Limitation: the repo was empty, so dedup against existing notes was not exercised.

Conventions exposed:
- The meaning of `date` was undefined. (resolved)
- Daily brief filename was undefined. (resolved)
- Sections added ad hoc, not in the templates (resolved):
  - News notes: "Watch Next" and "Unverified / Conflicting"
  - Daily brief: "Sources (summary-only items)"
- "Stale" has no time window. A 2026-08-26 story (DuckLabs → AWS) was retained as a first-run backfill.

Retention / importance:
- ACTION vs IMPORTANT depends on the user's actual stack (Next.js? vLLM? Claude Code with thinking disabled?), but no "my stack" list existed. (resolved)
- The ACTION rule ("update Topic note") conflicts with "human controls promotion". Topic updates were deferred. (resolved: after review)

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

Phase B, step B1 — owner review of the 7 inbox notes:

- set `status` on each note (`reviewed` / `retained` / `archived`)
- confirm or change the importance labels (including whether Sonnet 5.5 is `action`)

Topic notes (B2) follow only after that review.

## Guardrail

Do not add automation until the manual workflow has been tested with real news.

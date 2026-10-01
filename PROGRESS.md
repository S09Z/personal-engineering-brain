# PROGRESS.md

## Current State

Status: THIRD INGESTION PASS DONE — 9 News notes (7 retained, 2 inbox), 2 Topic notes, 2 daily briefs

## Current Phase

Phase 01 — Manual News Knowledge Base

## Current Loop

Phase D, step D2 — Docker / CI/CD coverage decided (complete, 2026-10-01)

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
- [x] Phase B1 (2026-10-01): review of the 7 inbox notes, delegated to the agent by the owner
  - all 7 notes set to `status: retained`; no importance label changed; nothing archived
  - OpenAI DevDay note rewritten from the official recap (read in a browser; plain fetch is blocked) and two statements corrected
  - Sonnet 5.5 stays `important`: the Claude Code setting change does not apply to the owner's setup
- [x] Phase B2 (2026-10-01): first Topic notes, only for topics with a retained `action` note
  - `20-topics/web-engineering.md` (two Next.js notes)
  - `20-topics/ai-infrastructure.md` (vLLM v0.30.0)
  - built from the retained News notes only; depends on the B1 statuses, so its PR is stacked on the B1 PR
- [x] Phase B3 (2026-10-01): `HOME.md` checked against the notes that exist
  - `web-engineering` and `ai-infrastructure` added to "Important Topics"; both open
  - one line added explaining that links without a note show as unresolved
- [x] Third ingestion pass (2026-10-01, second pass of the day):
  - 2 new News notes, both `inbox`: Gemini 4 Argon (`important`), PgBouncer 1.26.0 security release (`important`)
  - 3 routine releases kept summary-only (Node.js 22.23.3, Node.js 26.10.0, DuckDB 1.5.6)
  - existing notes checked for follow-ups; none needed
  - added as a "Second Pass" section in `40-summaries/daily/2026-10-01.md`; no new brief file
- [x] My Stack release checklist (2026-10-01):
  - `SOURCES.md`: new "My Stack Release Checklist" section — release and security pages for Next.js, Node.js, TypeScript, Claude Code, Codex, PostgreSQL, PgBouncer and vLLM, what to look for, and one optional `gh` command
  - `INGESTION_RULES.md`: the Discover step now says to check that list at every daily ingestion
  - a documented manual checklist, not automation; nothing added to `scripts/`
- [x] Phase D1 (2026-10-01): topic overlaps resolved with a Primary Topic Rule
  - `NEWS_REGISTRY.md`: new "Primary Topic Rule" section — the first entry in `topics` is primary and its theme is the note's `theme`; a table decides the primary topic for all 8 keywords listed under two topics; a rule for research papers vs `ai-papers`
  - `AGENTS.md`: `theme` and `topics` field meanings updated to match
  - DuckLabs note: topics reordered to `[databases, data-platforms]` (ownership of the engine → `databases`); same theme and folder
  - no keyword was removed from any topic
- [x] Phase D2 (2026-10-01): Docker / CI/CD coverage
  - decision: **no new Topic**; `Docker`, `CI/CD` and `infrastructure engineering` added as keywords of `developer-tooling`, plus one `track` line
  - reason: `INGESTION_RULES.md` §9 allows a new Topic only for a subject that appears repeatedly; no Docker or CI/CD story has been ingested yet
  - revisit: propose an `infrastructure-engineering` Topic once 3 retained News notes are filed under `developer-tooling` because of these keywords

## Phase D1 Findings

- The registry had 8 shared keywords, not 3: vLLM, Triton, inference, DuckDB, MCP, coding agent, vector database, reinforcement learning.
- 8 of the 9 existing notes already followed the rule; only the order of topics in the DuckLabs note changed.
- The check can verify that `theme` owns the first topic. It cannot verify that the first topic is the right one; that stays a judgment made with the table.
- Sonnet 5.5, DevDay and Gemini 4 Argon list `ai-coding-agents` (a software-engineering topic) second, under theme `llm`. That is allowed: only the primary topic must belong to the theme.

## Third Pass Findings

- **It was not a 2026-10-02 ingestion.** The pass was requested on 2026-10-01, when a brief for that day already existed and no market session had closed since. A brief dated 10-02 would have been falsely dated, so the pass was appended to the 10-01 brief. The count of daily briefs is still 2; Phase C needs 5.
- **Web search misses on-stack releases.** PgBouncer's security release (2026-09-23) and the Node.js and DuckDB releases were found only by listing GitHub releases and the postgresql.org news archive directly. (resolved: "My Stack Release Checklist" in `SOURCES.md`)
- **"My Stack" is too coarse for one case.** "PostgreSQL" does not say whether PgBouncer is in use, so the PgBouncer note could not be labelled `action` with confidence.
- **One brief per day vs. several passes.** The naming rule gives one brief per day. A "Second Pass" section worked, but is not a documented convention.
- The two Topic notes did not change: no retained note changed their "Current State".

## Phase B3 Findings

`HOME.md` link state after this step (19 links):

- 5 open: `web-engineering`, `ai-infrastructure`, `NEWS_REGISTRY`, `SOURCES`, `INGESTION_RULES`
- 14 are valid registry ids with no note yet: all 8 themes, and the topics `nasdaq`, `sp500`, `set50`, `ai-coding-agents`, `databases`, `local-llm`
- 0 point to something that is neither a file nor a registry id

Observations:

- No Theme note exists, so the whole "Core Themes" section is unresolved. Theme notes have no rule yet for when they are created.
- Clicking an unresolved link in Obsidian creates an empty note in the vault's default location, not in `20-topics/` or `30-themes/`. Worth setting when the vault is first opened.
- `ai-coding-agents` has two retained `important` notes (Sonnet 5.5, DevDay) but no Topic note, because B2 only covered topics with an `action` note.
- "Today" and "This Week" are plain folder paths; the daily briefs are not linked from `HOME.md`.

## Phase B2 Findings

- `templates/TOPIC.md` worked as is. One line was added under the title in each note: the registry id and what the topic covers.
- "Current State" is the useful section: it answers "what version should I be on" without reading the News notes.
- Two statements in the Topic notes come from GitHub data rather than a News note (Next.js advisory history, vLLM release cadence). Both sit under "Open Questions" and name their source.
- The vLLM note is filed under two topics; only `ai-infrastructure` got a note. `model-deployment` is linked but does not exist yet.
- Neither new topic is listed in `HOME.md` under "Important Topics".

## Phase B1 Review

Human-control note: the statuses below were proposed by the agent in a draft PR. Merging that PR is the owner's confirmation.

| Note | Importance | Status | Reason |
|---|---|---|---|
| 2026-09-30 Next.js September security release | action | retained | Security fixes on the stack; official sources |
| 2026-09-22 Next.js `next/og` RCE | action | retained | Critical fix on the stack; official advisory |
| 2026-09-22 vLLM v0.30.0 | action | retained | Breaking changes on the stack; official release notes |
| 2026-09-28 Claude Sonnet 5.5 | important | retained | Major model release; nothing to change locally |
| 2026-09-29 OpenAI DevDay 2026 | important | retained | Now verified against the official recap |
| 2026-08-26 DuckLabs joins AWS | important | retained | Ownership change of a core tool; official source |
| 2026-09-30 Micron fiscal Q4 2026 | important | retained | Major semiconductor-cycle earnings event; SEC filing |

Review findings:

- Secondary live coverage was wrong on two DevDay points (Codex "cloud-only"; Ultrafast tied to GPT-6.1 Sol). The official recap corrected both. Notes built only on live blogs should stay `inbox` until the primary source is read.
- The 2026-09-30 daily brief still carries the uncorrected DevDay wording ("cloud-only Codex"). Briefs were again left as a record of the day.
- No follow-up Next.js release for the deferred critical and high vulnerabilities as of this review.

## Loop 04 Findings

- Dedup against existing notes worked: a follow-up to a known event became an update, with an "Updates" section to keep the history. That section is not in the NEWS template yet.
- The earlier daily brief (2026-09-30) still says "nine vulnerabilities". Daily briefs were left as a record of what was known that day; this is not written down as a rule.
- The new `action` rule gave a clear answer: Micron earnings → `important` (nothing to do on the stack).
- Source conflict recorded in the note, not resolved: the GHSA-f87g-xv8r-7p7x advisory range and the 15.5.27 release notes disagree; advisory metadata gives patched versions as `16.3.?` / `15.5.?`.
- SET50 was missing for the second day. The SET Index fell 2.21%, kept in the daily brief as a routine move.

## Roadmap

Phases and sub-tasks agreed 2026-10-01:

- Phase A — Loop 04 (done)
- Phase B — B1 review of the 7 inbox notes (done); B2 first Topic notes for retained `action` items (done); B3 check HOME links (done)
- Phase C — after 5 daily briefs: weekly/monthly filenames, first weekly summary
- Phase D — registry and template cleanup: D1 topic overlaps (done); D2 Docker/CI-CD (done); still open: "stale" window, SET50 source, RESEARCH template, `.gitignore`)
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

- ~~Topic keyword overlaps in `NEWS_REGISTRY.md`~~ — resolved in Phase D1 by the Primary Topic Rule
- ~~Docker, CI/CD, infrastructure engineering not covered by any registry topic~~ — resolved in Phase D2 (keywords of `developer-tooling`)
- `templates/RESEARCH.md` lacks paper fields (title, authors, institution, benchmark, limitations)
- No MONTHLY template; weekly/monthly summary filenames undefined
- `.gitignore` missing `.env`, `.env.*`, `.obsidian/workspace*.json`
- `50-sources/` purpose undefined
- HOME.md links resolve only once the Topic/Theme notes exist

## Next Recommended Loop

Daily ingestion for 2026-10-02, run on or after that date:

- market snapshot for the 2026-10-01 sessions (US and SET)
- run the My Stack release checklist in `SOURCES.md`
- review the 2 inbox notes (Gemini 4 Argon, PgBouncer)
- follow-ups: deferred Next.js fixes, PostgreSQL 19 RC, DuckDB 2.0, Node.js 26 LTS

## Guardrail

Do not add automation until the manual workflow has been tested with real news.

---
type: news
status: inbox
date: 2026-09-28
event_date: 2026-09-28
theme: llm
topics: [foundation-models, ai-coding-agents]
importance: important
sources:
  - https://www.anthropic.com/claude-sonnet-5-5
  - https://platform.claude.com/docs/en/models/sonnet-5-5/overview
  - https://github.com/anthropics/claude-code/releases/tag/v2.1.284
---

# Anthropic releases Claude Sonnet 5.5

## Summary

- Claude Sonnet 5.5 (`claude-sonnet-5-5`) released 2026-09-28. It is the second model in the Claude 5.5 family, after Opus 5.5.
- Pricing is the same as stated for Sonnet: $2 / $10 per 1M input / output tokens. Anthropic claims it is 30%+ faster and up to 30% cheaper per task than Sonnet 5.
- Claude Haiku 5.5 is announced for "the coming weeks".

## What Happened

- Available on the Claude Platform, AWS, Google Cloud and Microsoft Azure.
- Pricing per 1M tokens: input $2, output $10, cache read $0.20, cache write $2.50.

## What Changed

Benchmarks below are **Anthropic's claims**, not independently verified:

- Terminal-Bench 4.0: 70.6% (Sonnet 5: 10.3%)
- CursorBench 4.0: 55.5%
- FrontierCode 1.1: 46.2% (Max effort)
- OSWorld 2.1: 80.1%
- GDPval-AA v2.1: 1844 (Opus 5.5: 1846)

Safety: Anthropic says this is the first Sonnet launched with classifiers that prevent reasoning extraction.

## Why It Matters

- It is a cheaper, faster default for everyday coding-agent work. Anthropic positions it as close to Opus 5.5 on some knowledge-work evals.

## Practical Impact

- **Claude Code:** per Anthropic, users running Sonnet with thinking disabled must switch to the `between_tools` setting before upgrading. This is a candidate for `action` if that applies to your setup.
- **Claude Code 2.1.284** (2026-09-28) makes Sonnet 5.5 the default Sonnet model on the Anthropic API, with a 1M context window. Added 2026-10-01.

## Watch Next

- Haiku 5.5 release.
- Independent benchmark results.

## Related Topics

- [[foundation-models|Foundation Models]]
- [[ai-coding-agents|AI Coding Agents]]

## Sources

- Anthropic, "Introducing Claude Sonnet 5.5", 2026-09-28 — official
- Claude Platform docs, Sonnet 5.5 model overview — official (found in search, not fetched)
- anthropics/claude-code release v2.1.284, 2026-09-28 — official

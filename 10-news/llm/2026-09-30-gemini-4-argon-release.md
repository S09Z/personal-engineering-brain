---
type: news
status: inbox
date: 2026-09-30
event_date: 2026-09-30
theme: llm
topics: [foundation-models, ai-coding-agents]
importance: important
sources:
  - https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/
  - https://techcrunch.com/2026/09/30/google-releases-gemini-4-argon-called-its-most-powerful-model-yet/
---

# Google announces Gemini 4 Argon; access limited to cyber-defense partners at first

## Summary

- Google announced Gemini 4 Argon on 2026-09-30, described as its frontier model for coding, enterprise knowledge work and cyber defense.
- **It is not generally available.** It is rolling out first to "trusted cyber defenders" through Google's Fairwind Program. General availability has no date ("as soon as possible").
- Announced pricing: $2 / $10 per 1M input / output tokens as an introductory price, then $4 / $20.

## What Happened

From Google's announcement (author: Koray Kavukcuoglu, Google DeepMind):

- **Availability:** Fairwind Program partners first. Google says it is taking part in the U.S. government's voluntary pre-release access process. The wider launch will start with paid API customers and Google AI Ultra subscribers.
- **Pricing:** introductory $2 input / $10 output per 1M tokens, cached input at a 95% discount. Standard pricing afterwards: $4 / $20.
- **Output limit:** a 1 million token output limit.

## What Changed

Benchmarks below are **Google's claims**, not independently verified:

- DeepSWE v1.1 (software engineering): 77.9%
- CWE-bench v1 (vulnerability remediation): 68%, tied for first
- AutomationBench: 51.3%, ranked first
- LVBench (long video understanding): 91.7%
- Vals Index: leading across finance, coding, legal and tax

## Why It Matters

- Three frontier model announcements landed in three days: Claude Sonnet 5.5 (09-28), GPT-6.1 Sol (09-29), Gemini 4 Argon (09-30).
- Sonnet 5.5 and Argon's introductory price are both $2 / $10 per 1M tokens. GPT-6.1 Sol's exact price was not verified; OpenAI states only "a fifth" of Astra's.
- Interpretation: with prices this close, near-term choice between these models is more about capability and availability than price.
- Releasing a frontier model to security partners before the public is a staged-access pattern worth tracking.

## Practical Impact

- Nothing to do on "My Stack": the model cannot be used yet.

## Unverified / Conflicting

- TechCrunch's claim that Argon beats OpenAI's and Anthropic's top models "across most benchmarks" was seen only in a search summary; the article was not read.
- The input context window size is not stated in what was read; only the 1M output limit is.
- The introductory price period has no stated end date.

## Watch Next

- General availability date and API model id.
- Independent benchmark results.
- Gemini CLI support.

## Related

- [[2026-09-28-claude-sonnet-5-5-release]]
- [[2026-09-29-openai-devday-2026]]

## Related Topics

- [[foundation-models|Foundation Models]]
- [[ai-coding-agents|AI Coding Agents]]

## Sources

- Google, "Gemini 4 Argon: our next era of frontier intelligence", 2026-09-30 — official
- TechCrunch, 2026-09-30 — independent reporting (found in search, not fetched)

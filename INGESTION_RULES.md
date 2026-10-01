# INGESTION_RULES.md

## Purpose

Defines how external information enters the Personal Engineering Brain.

Canonical pipeline:

DISCOVER
→ FILTER
→ DEDUPLICATE
→ VERIFY
→ SUMMARIZE
→ CLASSIFY
→ ASSIGN IMPORTANCE
→ RETAIN?
→ LINK TOPIC
→ PROMOTE?

---

# 1. Discover

Supported V1 inputs:

- RSS / Atom
- Obsidian Web Clipper
- manually supplied URL
- web search result
- official release note
- GitHub release
- research paper

Do not scrape aggressively when a stable feed or official source exists.

---

# 2. Filter

Reject early when an item is:

- irrelevant to `NEWS_REGISTRY.md`
- duplicate marketing material
- low-signal commentary
- unsupported rumor
- obvious SEO content
- stale with no new information

---

# 3. Deduplicate

Before creating a permanent note, search for:

- same URL
- same event
- same release
- same company/product
- same paper
- same event date

Multiple reports about the same event should usually become one canonical note with multiple sources.

---

# 4. Verify

Prefer the strongest available source.

For product/release news:
- official announcement
- release notes
- documentation
- repository

For markets:
- exchange/regulator/company filing
- reputable financial reporting

For research:
- paper
- official repository
- project page

Community discussion is supplementary evidence only.

---

# 5. Summarize

Summaries should answer:

- What happened?
- What changed?
- Why does it matter?
- Who or what is affected?
- What should be watched next?

Keep summaries concise.

Do not reproduce full articles.

---

# 6. Classify

Assign:

- Theme
- Topic(s)
- importance
- event date
- publication date
- source(s)

Use canonical names from `NEWS_REGISTRY.md`.

---

# 7. Importance

Allowed values:

## ACTION

Immediate practical impact on the tools listed under "My Stack" in `NEWS_REGISTRY.md`.

Examples:

- security vulnerability
- breaking API change
- major dependency deprecation
- production-impacting release

## IMPORTANT

Meaningful development worth retaining.

## INTERESTING

Useful context, usually summary-only.

## IGNORE

Do not retain.

---

# 8. Retention

ACTION:
- permanent News note
- update Topic note after human review of the News note

IMPORTANT:
- permanent News note
- link to Topic

INTERESTING:
- Daily or Weekly summary by default

IGNORE:
- discard

---

# 9. Topic Promotion

Create a new Topic only when:

- it appears repeatedly
- it is important enough to query independently
- it is likely to accumulate future developments

Do not create a Topic for every company, article, feature, or minor release.

---

# 10. Financial News

Routine index moves belong in Daily summaries.

Promote only when there is a meaningful event such as:

- major earnings surprise
- material guidance change
- major macro shock
- index composition change
- major regulatory event
- substantial AI/technology capex shift
- major semiconductor cycle event

Do not convert normal daily volatility into permanent knowledge.

---

# 11. Research News

Promote a paper when at least one is true:

- major architectural contribution
- important benchmark result
- strong practical relevance
- influential research lab
- likely impact on engineering practice
- repeatedly referenced by later work

Record limitations and avoid presenting author claims as independently verified facts.

---

# 12. Human Review

V1 should prefer human review before permanent promotion.

Automation may prepare:

- summary
- classification
- duplicate candidates
- suggested topics

Human decides whether to retain/promote until the workflow is proven reliable.

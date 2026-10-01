# SOURCES.md

## Source Strategy

Use the strongest source available and avoid collecting the same story from many low-value sources.

---

# Tier 1 — Primary / Official

## Markets

- Nasdaq
- S&P Global
- Stock Exchange of Thailand
- SEC (US)
- SEC Thailand
- Bank of Thailand
- company investor relations
- company filings

## Software Engineering

- official project blogs
- official release notes
- GitHub releases
- security advisories
- official documentation

## AI / LLM

- OpenAI
- Anthropic
- Google DeepMind
- Meta AI
- Microsoft Research
- NVIDIA
- Hugging Face
- official model/project repositories

## AI Research

- arXiv
- NeurIPS
- ICML
- ICLR
- ACL
- EMNLP
- CVPR
- ICCV
- ECCV
- official lab pages
- author repositories

---

# Tier 2 — Reputable Independent Reporting

Examples:

- Reuters
- Bloomberg
- Financial Times
- Ars Technica
- selected engineering publications

Use these for context and independent confirmation.

---

# Tier 3 — Community Signals

Examples:

- Hacker News
- Reddit
- GitHub Issues
- forums
- social posts

Use for discovery and practitioner experience.

Do not treat community commentary as established fact without verification.

---

# Source Selection Rules

Prefer:

official source + one strong independent source

over:

many repetitive summaries

For a single event, preserve multiple sources in one canonical note rather than creating duplicate notes.

---

# My Stack Release Checklist

Check these pages directly at every daily ingestion. Web search does not reliably surface releases of the tools in "My Stack" (`NEWS_REGISTRY.md`): a PgBouncer security release was missed for a week that way.

Keep this list in step with "My Stack". Add a tool here only when it is added there.

## Next.js / Node.js / TypeScript

| Tool | Releases | Security |
|---|---|---|
| Next.js | https://github.com/vercel/next.js/releases | https://github.com/vercel/next.js/security/advisories and https://nextjs.org/blog |
| Node.js | https://github.com/nodejs/node/releases | https://nodejs.org/en/blog/vulnerability |
| TypeScript | https://github.com/microsoft/TypeScript/releases | — |

## Coding agents

| Tool | Releases | Announcements |
|---|---|---|
| Claude Code | https://github.com/anthropics/claude-code/releases | https://www.anthropic.com/news |
| Codex | https://github.com/openai/codex/releases | — |

## PostgreSQL

| Tool | Releases | Security |
|---|---|---|
| PostgreSQL | https://www.postgresql.org/about/newsarchive/ | https://www.postgresql.org/support/security/ |
| PgBouncer (if used) | https://github.com/pgbouncer/pgbouncer/releases | https://www.pgbouncer.org/changelog.html |

The PostgreSQL news archive also carries ecosystem releases such as PgBouncer.

## Self-hosted inference

| Tool | Releases |
|---|---|
| vLLM | https://github.com/vllm-project/vllm/releases |

## What to look for

- a security fix → candidate for `action`
- breaking changes, removed flags or settings → candidate for `action`
- a new major or LTS version → usually `important`
- routine point releases → daily brief only, or ignore

Compare against the versions already recorded in the Topic notes and the last daily brief, so only releases since the last check are considered.

## Optional: list the latest stable releases in one command

Needs the GitHub CLI (`gh`). It prints the three most recent non-prerelease tags per repository. PostgreSQL itself is not on GitHub releases; check its news archive by hand.

```bash
for r in vercel/next.js nodejs/node microsoft/TypeScript anthropics/claude-code openai/codex vllm-project/vllm pgbouncer/pgbouncer; do
  echo "== $r"
  gh api "repos/$r/releases?per_page=30" --jq '[.[] | select(.prerelease | not)][0:3][] | "\(.published_at[0:10])  \(.tag_name)"'
done
```

---

# Daily Market Snapshot Sources

## SET and SET50

Use the Stock Exchange of Thailand (official). Both pages are on set.or.th.

| Page | What it gives | How to read it |
|---|---|---|
| https://www.set.or.th/en/market/statistics/five-days | Closing level and % change for SET, SET50 and other indexes for the last five trading days; trading volume and value | Needs a real browser. A plain fetch returns the page without the numbers. |
| https://www.set.or.th/en/market/index/set50/overview | SET50 last value, change, % change, high, low, with an "as of" time | A plain fetch works. |

Notes:

- SET states that the day's figures are officially updated at around 18:30 Bangkok time. Before that, the last column is a live value, not a close.
- On the overview page, the previous close is the last value minus the change.
- Thai financial news (for example Kaohoon International's daily "Market Roundup") reports the SET Index and the analyst view of drivers, but not SET50. Use it for drivers, and the exchange for levels.

---
type: news
status: inbox
date: 2026-09-23
event_date: 2026-09-30
theme: software-engineering
topics: [web-engineering]
importance: action
sources:
  - https://nextjs.org/blog/upcoming-nextjs-security-release-september-2026
  - https://github.com/vercel/next.js/releases
---

# Next.js scheduled security release: 9 vulnerabilities, 16.3.8 / 15.5.27 (2026-09-30)

## Summary

- Next.js pre-announced a security release for 2026-09-30 fixing 9 vulnerabilities (1 critical, 2 high, 5 medium, 1 low).
- Patched versions will be **16.3.8** and **15.5.27**. Full advisories publish with the release.
- **16.3.7 (2026-09-29) does NOT contain these fixes.** It is a bug-fix release only.

## What Happened

- 2026-09-23: advance notice published on the Next.js blog (authors: Josh Story, Karim Rahal, Sebastian Silbermann).
- 2026-09-29: the notice was updated. 16.3.7 shipped with a bug fix only, and the security fixes moved to 16.3.8 / 15.5.27.
- As of 2026-09-30 ingestion, GitHub releases show no 16.3.8 yet (latest: `v16.3.7`, `v16.4.0-canary.53`).

## What Changed

- Nothing is patched yet. This note records the advance notice and the expected patch versions.

## Why It Matters

- The batch includes a critical vulnerability. Details (affected versions, impact) are not yet public.

## Practical Impact

- Any Next.js 15.x / 16.x app should be upgraded to 15.5.27 / 16.3.8 once they are published.
- Do not treat 16.3.7 as the security fix.

## Watch Next

- Publication of 16.3.8 / 15.5.27 and the 9 GHSA advisories. Update this note with the advisory IDs.

## Related

- Separate, earlier event: [[2026-09-22-nextjs-og-imageresponse-rce]] (fixed in 16.3.6; not part of this batch)

## Related Topics

- [[web-engineering|Web Engineering]]

## Sources

- Next.js blog, "Upcoming Next.js September Security Release", published 2026-09-23, updated 2026-09-29 — official
- vercel/next.js GitHub releases, checked 2026-09-30 — official

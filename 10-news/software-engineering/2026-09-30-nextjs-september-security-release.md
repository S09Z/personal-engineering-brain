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
  - https://github.com/vercel/next.js/releases/tag/v16.3.8
  - https://github.com/vercel/next.js/releases/tag/v15.5.27
  - https://github.com/vercel/next.js/security/advisories
---

# Next.js September security release: 7 vulnerabilities fixed in 16.3.8 / 15.5.27

## Summary

- Next.js **16.3.8** and **15.5.27** were published 2026-09-30 and fix 7 vulnerabilities: 1 high, 5 medium, 1 low.
- The release was announced as 9 fixes. The **critical** one and one **high** were held back and are still unpatched; Vercel says they will come in a later release.
- 16.3.7 (2026-09-29) contains none of these fixes.

## Updates

- 2026-10-01: note updated after the release. Scope changed from 9 to 7; versions and advisory IDs added.
- 2026-09-30: note created from the advance notice, before the patches were out.

## What Happened

- 2026-09-23: advance notice published on the Next.js blog (authors: Josh Story, Karim Rahal, Sebastian Silbermann).
- 2026-09-29: notice updated. 16.3.7 shipped with a bug fix only.
- 2026-09-30: notice updated again. The release covers seven vulnerabilities, not nine; the other two are "pending upstream coordination".
- 2026-09-30 16:13 UTC: `v16.3.8` and `v15.5.27` published on GitHub, with seven advisories.

## What Changed

Fixed in 16.3.8 (per its release notes):

| Severity | Advisory | CVE | Issue |
|---|---|---|---|
| high | GHSA-cjq9-62q9-8jv4 | CVE-2026-94483 | SSRF in Image Optimization |
| medium | GHSA-f87g-xv8r-7p7x | CVE-2026-94485 | Information disclosure in App Router metadata image routes |
| medium | GHSA-4jqv-mc3x-m676 | CVE-2026-94543 | Cache poisoning of SSG/ISR pages in self-hosted apps |
| medium | GHSA-mcj8-r9mp-w47p | CVE-2026-94484 | Cache poisoning in SSG/ISR rendering (content substitution, persistent DoS) |
| medium | GHSA-3w37-wq28-93x7 | CVE-2026-94544 | `use cache` fill can leak Draft Mode content |
| medium | GHSA-h694-7cp9-m8p3 | none yet | Cache leak across root param values in nested `use cache` |
| low | GHSA-39w2-rjm5-chcv | CVE-2026-94486 | Information disclosure in the dev server's MCP endpoint |

Fixed in 15.5.27 (per its release notes): GHSA-f87g-xv8r-7p7x, GHSA-4jqv-mc3x-m676, GHSA-mcj8-r9mp-w47p.

## Why It Matters

- The high-severity SSRF and the two cache-poisoning issues affect self-hosted production apps.
- A critical and a high vulnerability are known to exist and are not yet fixed. No details are public.

## Practical Impact

- Upgrade 16.x apps to **16.3.8** and 15.x apps to **15.5.27**.
- Expect another security release for the two deferred issues.

## Unverified / Conflicting

- The advisory metadata lists patched versions as `16.3.?` / `15.5.?`, not exact numbers. The exact versions above come from the release notes.
- GHSA-f87g-xv8r-7p7x is listed in the 15.5.27 release notes, but its advisory gives the affected range as `>= 16.0.0` only.

## Watch Next

- The follow-up release for the deferred critical and high vulnerabilities.

## Related

- Separate, earlier event: [[2026-09-22-nextjs-og-imageresponse-rce]] (fixed in 16.3.6; not part of this batch)

## Related Topics

- [[web-engineering|Web Engineering]]

## Sources

- Next.js blog, "Upcoming Next.js September Security Release", published 2026-09-23, updated 2026-09-29 and 2026-09-30 — official
- vercel/next.js release notes for v16.3.8 and v15.5.27, 2026-09-30 — official
- vercel/next.js GitHub security advisories, published 2026-09-30 — official

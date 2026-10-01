---
type: news
status: inbox
date: 2026-09-22
event_date: 2026-09-22
theme: software-engineering
topics: [web-engineering]
importance: action
sources:
  - https://github.com/vercel/next.js/security/advisories/GHSA-vcvr-r3jv-pc5j
---

# Next.js critical RCE in `next/og` ImageResponse (CVE-2026-94545), fixed in 16.3.6

## Summary

- Critical remote code execution in the Node.js `ImageResponse` implementation from `next/og`, caused by an upstream vulnerability.
- Affected: `next` >= 16.2.0, < 16.3.6. Patched: **16.3.6**.
- Only apps that pass attacker-controlled values into SVG content, attributes or styles during image generation are affected.

## What Happened

- 2026-09-22: GHSA-vcvr-r3jv-pc5j / CVE-2026-94545 published by Vercel. Severity: critical.

## What Changed

- 16.3.6 contains the fix.

## Why It Matters

- RCE in a commonly used feature (OG image generation), reachable through request parameters in the pattern the advisory shows.

## Practical Impact

- Check Next.js apps on 16.2.x–16.3.5 for Node.js-runtime `ImageResponse` routes that use request input.
- Not affected: the Edge `ImageResponse` implementation, and apps that do not pass attacker-controlled values into SVG.
- Workaround if you cannot upgrade: stop passing untrusted values into SVG content, attributes or styles.

## Related

- Separate, later event: [[2026-09-30-nextjs-september-security-release]]. It is a different batch with different patch versions. Kept as its own note on purpose.

## Related Topics

- [[web-engineering|Web Engineering]]

## Sources

- GitHub Security Advisory GHSA-vcvr-r3jv-pc5j, published 2026-09-22 — official

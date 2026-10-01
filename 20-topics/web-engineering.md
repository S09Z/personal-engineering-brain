---
type: topic
status: active
theme: software-engineering
updated: 2026-10-01
---

# Web Engineering

Registry id: `web-engineering`. Covers Node.js, TypeScript, Next.js, React and related build tooling.

## Current State

- **Next.js patched versions:** 16.3.8 (16.x line) and 15.5.27 (15.x line), both published 2026-09-30.
- **Known unpatched:** one critical and one high Next.js vulnerability are announced but not yet fixed. No details are public; Vercel says they will come in a later release.
- Nothing is recorded yet for Node.js, TypeScript or the other tools in this topic.

## Key Developments

- **2026-09-30 — Next.js September security release.** 16.3.8 / 15.5.27 fix 7 vulnerabilities (1 high, 5 medium, 1 low): SSRF in Image Optimization, cache poisoning of SSG/ISR pages, `use cache` leaks. The release was announced as 9 fixes; two were held back. → [[2026-09-30-nextjs-september-security-release]]
- **2026-09-22 — Critical RCE in `next/og` ImageResponse (CVE-2026-94545).** Affects 16.2.0 up to 16.3.5 when attacker-controlled values reach SVG output in the Node.js runtime. Fixed in 16.3.6. → [[2026-09-22-nextjs-og-imageresponse-rce]]

## Recent News

- [[2026-09-30-nextjs-september-security-release]] — action
- [[2026-09-22-nextjs-og-imageresponse-rce]] — action

## Practical Impact

- Run 16.x apps on **16.3.8 or later** and 15.x apps on **15.5.27 or later**. 16.3.8 is later than 16.3.6, so it also contains the `next/og` fix.
- 16.3.7 is a bug-fix release only; it is not a security baseline.
- Self-hosted apps are the ones exposed to the cache-poisoning issues.
- Plan for one more security upgrade soon.

## Open Questions

- When will the deferred critical and high Next.js fixes ship, and which versions are affected?
- One advisory (GHSA-f87g-xv8r-7p7x) lists only 16.x as affected, yet the 15.5.27 release notes list it as fixed. Which is right?
- GitHub's advisory list shows critical Next.js advisories in both August and September 2026. Whether that is a trend worth a different upgrade policy is not established.

## Related Topics

- [[ai-coding-agents|AI Coding Agents]] — one of the September fixes concerns the Next.js dev server's MCP endpoint

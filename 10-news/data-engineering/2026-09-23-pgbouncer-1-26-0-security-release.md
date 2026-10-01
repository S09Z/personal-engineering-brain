---
type: news
status: inbox
date: 2026-09-23
event_date: 2026-09-23
theme: data-engineering
topics: [databases]
importance: important
sources:
  - https://www.postgresql.org/about/news/pgbouncer-1260-released-fixes-three-cves-3385
  - https://www.pgbouncer.org/2026/09/pgbouncer-1-26-0
---

# PgBouncer 1.26.0 fixes three denial-of-service CVEs

## Summary

- PgBouncer 1.26.0 (2026-09-23) fixes three denial-of-service vulnerabilities. Two can be triggered by **unauthenticated clients**.
- The release also removes the deprecated online restart (`-R`) option.
- **Importance depends on your setup:** this is `action` if you run PgBouncer in front of PostgreSQL. It is labelled `important` because that is not known.

## What Happened

| CVE | Impact | Who can trigger it | Cause |
|---|---|---|---|
| CVE-2026-19888 | Crash | Unauthenticated client | SCRAM client-final-message without a nonce |
| CVE-2026-6668 | Infinite loop | Unauthenticated client | Integer overflow in packet buffer growth |
| CVE-2026-6669 | Unbounded work during login | Malicious PostgreSQL server | Unbounded SCRAM iteration count |

## What Changed

- `search_path` and `default_transaction_read_only` are now tracked by default.
- New `pool_idle_timeout` setting.
- `query_wait_timeout` can be set per user and per database.
- Meson build support added.
- **Removed:** online restart (`-R`).

## Why It Matters

- A connection pooler is usually reachable by every application client. A crash or hang there takes down database access for all of them.

## Practical Impact

- If you run PgBouncer: upgrade to 1.26.0. The project recommends it especially for instances that accept connections from untrusted networks or connect to untrusted PostgreSQL servers.
- Check for any tooling that still uses `-R` before upgrading.

## Unverified / Conflicting

- Affected version ranges are not stated in the announcement that was read.
- The pgbouncer.org changelog was not fetched; details here come from the postgresql.org announcement.

## Watch Next

- PostgreSQL 19 release candidate (early October) and GA.

## Related Topics

- [[databases|Databases]]

## Sources

- PostgreSQL.org news, "PgBouncer 1.26.0 released - Fixes three CVEs", 2026-09-23 — official project announcement
- pgbouncer.org changelog for 1.26.0 — official (linked from the announcement, not fetched)

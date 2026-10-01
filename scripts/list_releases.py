#!/usr/bin/env python3
"""List recent stable releases of the tools in the My Stack Release Checklist.

The repositories are read from the "My Stack Release Checklist" section of SOURCES.md,
so that section stays the only list to maintain.

Usage:
    python3 scripts/list_releases.py                     # releases in the last 14 days
    python3 scripts/list_releases.py --since 2026-09-24  # releases on or after a date

It only prints a list. It does not create or change any note; deciding what a release
means is still done by reading it. Standard library only.

GitHub allows 60 unauthenticated API requests per hour; this makes one per repository.
Set GITHUB_TOKEN to raise the limit.
"""

import argparse
import datetime
import json
import os
import pathlib
import re
import sys
import urllib.error
import urllib.request

SECTION_START = "# My Stack Release Checklist"
STALE_WINDOW_DAYS = 14  # same window as "Stale window" in INGESTION_RULES.md


def checklist_section(root):
    """Return the text of the checklist section of SOURCES.md."""
    text = (root / "SOURCES.md").read_text()
    if SECTION_START not in text:
        sys.exit(f"SOURCES.md has no '{SECTION_START}' section")
    section = text.split(SECTION_START, 1)[1]
    # The section ends at the next top-level heading.
    return re.split(r"^# ", section, maxsplit=1, flags=re.M)[0]


def checklist_urls(section):
    urls = re.findall(r"https://[^\s|)]+", section)
    return list(dict.fromkeys(urls))  # unique, in document order


def split_urls(urls):
    """Return (GitHub 'owner/repo' names with a releases page, every other URL)."""
    repos, by_hand = [], []
    for url in urls:
        match = re.match(r"^https://github\.com/([^/]+/[^/]+)/releases$", url)
        if match:
            repos.append(match.group(1))
        else:
            by_hand.append(url)
    return repos, by_hand


def fetch_releases(repo):
    request = urllib.request.Request(
        f"https://api.github.com/repos/{repo}/releases?per_page=50",
        headers={"Accept": "application/vnd.github+json", "User-Agent": "personal-engineering-brain"},
    )
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--since", help="YYYY-MM-DD; default is 14 days ago")
    args = parser.parse_args()

    today = datetime.date.today()
    if args.since:
        try:
            since = datetime.date.fromisoformat(args.since)
        except ValueError:
            sys.exit(f"--since must be YYYY-MM-DD, got '{args.since}'")
    else:
        since = today - datetime.timedelta(days=STALE_WINDOW_DAYS)

    root = pathlib.Path(__file__).resolve().parent.parent
    repos, by_hand = split_urls(checklist_urls(checklist_section(root)))

    print(f"Stable releases published on or after {since} (today is {today})\n")
    errors = 0
    for repo in repos:
        print(f"== {repo}")
        try:
            releases = fetch_releases(repo)
        except (urllib.error.URLError, json.JSONDecodeError) as error:
            errors += 1
            print(f"   ERROR: could not read releases: {error}")
            continue
        recent = [
            r for r in releases
            if not r["prerelease"] and not r["draft"] and r["published_at"][:10] >= since.isoformat()
        ]
        if not recent:
            print("   none")
        for release in recent:
            print(f"   {release['published_at'][:10]}  {release['tag_name']}  {release['html_url']}")

    print("\nNot covered by this script. Check these pages by hand:")
    for url in by_hand:
        print(f"   {url}")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())

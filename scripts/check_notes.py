#!/usr/bin/env python3
"""Validate the notes in this vault against the rules in AGENTS.md and NEWS_REGISTRY.md.

Usage:
    python3 scripts/check_notes.py            # check this repository
    python3 scripts/check_notes.py PATH       # check a copy of the vault at PATH

Exit code 0 when every check passes, 1 otherwise.
Standard library only. It reads files and never changes them.
"""

import pathlib
import re
import sys

IMPORTANCE = {"action", "important", "interesting"}
STATUS = {"inbox", "reviewed", "retained", "archived"}
NEWS_FIELDS = ["type", "date", "event_date", "theme", "topics", "importance", "status", "sources"]
LINK = re.compile(r"\[\[([^\]|]+)")

failures = []


def fail(path, message):
    failures.append(f"FAIL {path}: {message}")


def frontmatter(path):
    """Return the text between the first two '---' lines, or '' if there is none."""
    parts = path.read_text().split("---")
    return parts[1] if len(parts) >= 3 else ""


def field(fm, key):
    """Return the value on the 'key:' line of a frontmatter block, or None if the key is absent."""
    match = re.search(rf"^{key}:[ \t]*(.*)$", fm, re.M)
    return match.group(1).strip() if match else None


def read_registry(root):
    """Return (theme ids, {topic id: owning theme id}) from NEWS_REGISTRY.md."""
    themes, topic_theme = set(), {}
    current_theme, expecting = None, None
    for line in (root / "NEWS_REGISTRY.md").read_text().splitlines():
        if line.startswith("# THEME:"):
            expecting = "theme"
        elif line.startswith("## Topic:"):
            expecting = "topic"
        elif line.startswith("id: ") and expecting:
            value = line[4:].strip()
            if expecting == "theme":
                themes.add(value)
                current_theme = value
            else:
                topic_theme[value] = current_theme
            expecting = None
    return themes, topic_theme


def check_news(root, news, themes, topic_theme):
    for path in news:
        rel = path.relative_to(root)
        fm = frontmatter(path)
        for key in NEWS_FIELDS:
            if field(fm, key) is None:
                fail(rel, f"missing frontmatter field '{key}'")

        if field(fm, "type") != "news":
            fail(rel, "type must be 'news'")
        if field(fm, "importance") not in IMPORTANCE:
            fail(rel, f"importance '{field(fm, 'importance')}' is not one of {sorted(IMPORTANCE)}")
        if field(fm, "status") not in STATUS:
            fail(rel, f"status '{field(fm, 'status')}' is not one of {sorted(STATUS)}")

        theme = field(fm, "theme")
        if theme not in themes:
            fail(rel, f"theme '{theme}' is not a registry theme id")
        if path.parent.name != theme:
            fail(rel, f"file is in folder '{path.parent.name}' but theme is '{theme}'")

        topics = re.findall(r"[\w-]+", field(fm, "topics") or "")
        if not topics:
            fail(rel, "topics is empty")
        for topic in topics:
            if topic not in topic_theme:
                fail(rel, f"topic '{topic}' is not a registry topic id")
        if len(topics) != len(set(topics)):
            fail(rel, "a topic is listed twice")
        # Primary Topic Rule: the first topic decides the theme.
        if topics and topics[0] in topic_theme and topic_theme[topics[0]] != theme:
            fail(rel, f"theme '{theme}' does not own the primary topic '{topics[0]}' "
                      f"(owner: '{topic_theme[topics[0]]}')")

        if not re.match(r"^\d{4}-\d{2}-\d{2}-[a-z0-9-]+$", path.stem):
            fail(rel, "filename must be YYYY-MM-DD-short-description.md")
        if path.stem[:10] != field(fm, "event_date"):
            fail(rel, "date in filename must equal event_date")
        if not re.search(r"^sources:\s*\n\s+- https?://", fm, re.M):
            fail(rel, "sources must list at least one URL")


def check_topics(root, topic_notes, news, topic_theme):
    retained = {p.stem for p in news if field(frontmatter(p), "status") == "retained"}
    news_names = {p.stem for p in news}
    for path in topic_notes:
        rel = path.relative_to(root)
        fm = frontmatter(path)
        text = path.read_text()

        if path.stem not in topic_theme:
            fail(rel, "filename is not a registry topic id")
            continue
        if field(fm, "type") != "topic":
            fail(rel, "type must be 'topic'")
        if field(fm, "theme") != topic_theme[path.stem]:
            fail(rel, f"theme must be '{topic_theme[path.stem]}'")
        if not re.match(r"^\d{4}-\d{2}-\d{2}$", field(fm, "updated") or ""):
            fail(rel, "updated must be a YYYY-MM-DD date")

        linked = set(LINK.findall(text))
        # A Topic note cites only retained news...
        for target in sorted(linked & news_names):
            if target not in retained:
                fail(rel, f"links news note '{target}' whose status is not 'retained'")
        # ...and cites every retained news note filed under this topic.
        for note in news:
            note_topics = re.findall(r"[\w-]+", field(frontmatter(note), "topics") or "")
            if path.stem in note_topics and note.stem in retained and note.stem not in linked:
                fail(rel, f"retained news note '{note.stem}' is not linked")


def check_links(root, files, news, topic_theme, themes):
    """Every [[link]] must point to a news note, a registry id, or an existing Markdown file."""
    known = {p.stem for p in news} | set(topic_theme) | themes
    for path in files:
        rel = path.relative_to(root)
        for target in LINK.findall(path.read_text()):
            if target not in known and not (root / f"{target}.md").exists():
                fail(rel, f"unresolved link [[{target}]]")


def check_home(root, topic_notes):
    """Every Topic note must be reachable from HOME.md."""
    home = root / "HOME.md"
    linked = set(LINK.findall(home.read_text()))
    for path in topic_notes:
        if path.stem not in linked:
            fail("HOME.md", f"Topic note '{path.stem}' is not linked")


def main():
    default_root = pathlib.Path(__file__).resolve().parent.parent
    root = pathlib.Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else default_root

    themes, topic_theme = read_registry(root)
    news = sorted((root / "10-news").rglob("*.md"))
    topic_notes = sorted((root / "20-topics").glob("*.md"))
    summaries = sorted((root / "40-summaries").rglob("*.md"))

    check_news(root, news, themes, topic_theme)
    check_topics(root, topic_notes, news, topic_theme)
    check_links(root, news + topic_notes + summaries + [root / "HOME.md"], news, topic_theme, themes)
    check_home(root, topic_notes)

    for line in failures:
        print(line)
    print(f"registry: {len(themes)} themes, {len(topic_theme)} topics")
    print(f"checked: {len(news)} news notes, {len(topic_notes)} topic notes, "
          f"{len(summaries)} summaries, HOME.md")
    print(f"failures: {len(failures)}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())

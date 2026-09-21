#!/usr/bin/env python3
"""Create a new blog post or note.

    python scripts/new.py post "Title of the post"
    python scripts/new.py note "Title of the note" -c R -c "Data wrangling"

New items are created as drafts (draft: true), so nothing goes live by accident.
When you are happy with it, delete the `draft: true` line and push.
Use --publish to skip the draft step.
"""
import argparse
import datetime
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FOLDERS = {"post": ROOT / "blog" / "posts", "note": ROOT / "notes" / "posts"}


def slugify(title: str) -> str:
    text = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return text or "untitled"


def yaml_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("kind", choices=sorted(FOLDERS), help="post (Blog) or note (Notes)")
    parser.add_argument("title")
    parser.add_argument("-c", "--category", action="append", default=[], help="repeat for several categories")
    parser.add_argument("-d", "--description", default="", help="one line shown in the listing")
    parser.add_argument("--publish", action="store_true", help="create it ready to publish (no draft flag)")
    args = parser.parse_args()

    folder = FOLDERS[args.kind] / slugify(args.title)
    target = folder / "index.qmd"
    if target.exists():
        print(f"Already exists: {target.relative_to(ROOT)}", file=sys.stderr)
        return 1

    lines = [
        "---",
        f"title: {yaml_quote(args.title)}",
        f"date: {datetime.date.today().isoformat()}",
        f"description: {yaml_quote(args.description)}",
    ]
    if args.category:
        lines.append("categories: [" + ", ".join(args.category) + "]")
    if not args.publish:
        lines.append("draft: true            # delete this line to publish")
    lines += ["---", "", "Write here.", ""]

    folder.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(lines), encoding="utf-8")
    print(f"Created {target.relative_to(ROOT)}")
    print("Preview with:  quarto preview")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Prepend a "logos synced" entry to assets/updates.json.

Called by the daily sync workflow (.github/workflows/sync-logos.yml) whenever it
pulls new/changed logo files from upstream, so the website notification bell, the
Updates page, and the Figma plugin all surface what arrived — automatically.

Each entry gets a stable, unique ``id`` (``sync-<seq>``) so the unread dot fires
even when several updates land on the same calendar day.
"""
import argparse
import datetime
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPDATES = os.path.join(ROOT, "assets", "updates.json")
MAX_ENTRIES = 60


def plural(n, word):
    return "%d %s%s" % (n, word, "" if n == 1 else "s")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--added", type=int, default=0)
    ap.add_argument("--updated", type=int, default=0)
    ap.add_argument("--removed", type=int, default=0)
    ap.add_argument("--names", default="", help="comma-separated sample of added logo slugs")
    ap.add_argument("--date", default="", help="YYYY-MM-DD (defaults to today, UTC)")
    args = ap.parse_args()

    if args.added == 0 and args.updated == 0 and args.removed == 0:
        print("log_sync: nothing changed — no entry added.")
        return

    date = args.date or datetime.datetime.utcnow().strftime("%Y-%m-%d")

    with open(UPDATES, encoding="utf-8") as f:
        data = json.load(f)
    entries = data.get("entries", [])
    seq = int(data.get("seq", 0)) + 1

    # headline
    if args.added:
        title = plural(args.added, "new logo") + " added"
        tag = "new"
    elif args.updated:
        title = plural(args.updated, "logo") + " refreshed"
        tag = "improved"
    else:
        title = plural(args.removed, "logo") + " removed"
        tag = "improved"

    # body — summary + a few names
    parts = []
    if args.added:
        parts.append("%d added" % args.added)
    if args.updated:
        parts.append("%d updated" % args.updated)
    if args.removed:
        parts.append("%d removed" % args.removed)
    summary = ", ".join(parts)
    body = "Auto-synced from the upstream collection — %s." % summary

    names = [n.strip().replace("-", " ") for n in args.names.split(",") if n.strip()]
    if names:
        more = "…" if args.added > len(names) else ""
        body += " New: %s%s." % (", ".join(names[:6]), more)

    entry = {"date": date, "tag": tag, "id": "sync-%d" % seq, "title": title, "body": body}
    entries.insert(0, entry)
    data["entries"] = entries[:MAX_ENTRIES]
    data["seq"] = seq

    with open(UPDATES, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print("log_sync: added '%s' (id sync-%d)." % (title, seq))


if __name__ == "__main__":
    main()

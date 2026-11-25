#!/usr/bin/env python3
"""Checks run before a post is published. Exits 1 if anything fails.

- every internal link and asset on every built page resolves
- every post body uses only the allowed tags, names no employer, has no em dashes,
  and is a sensible length
Usage: python3 tools/check_site.py [--strict-slug SLUG]
With --strict-slug, that post must also contain no <mark class="todo"> passages.
"""
import glob
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
os.chdir(ROOT)
problems, notes = [], []

for f in glob.glob("**/index.html", recursive=True) + ["404.html"]:
    s = open(f, encoding="utf-8").read()
    d = os.path.dirname(f)
    for u in re.findall(r'(?:href|src)="([^"#]+)', s):
        if u.startswith(("http", "mailto:", "data:")):
            continue
        u = u.split("?")[0]
        t = os.path.normpath(os.path.join(d, u)) if not u.startswith("/") else u.lstrip("/")
        if u.endswith("/") or u in (".", "..") or os.path.isdir(t):
            t = os.path.join(t, "index.html")
        if not os.path.exists(t):
            problems.append(f"broken link in {f}: {u}")

strict = sys.argv[sys.argv.index("--strict-slug") + 1] if "--strict-slug" in sys.argv else None
ALLOWED = {"p", "h2", "h3", "ul", "ol", "li", "strong", "em", "a", "blockquote", "mark"}
EMPLOYERS = r"Stripe|Shopify|Fullscript|IRCC|EDC|Canadian Heritage|Export Development|Immigration, Refugees"
for f in sorted(glob.glob("posts/*.html")):
    slug = os.path.basename(f)[:-5]
    s = open(f, encoding="utf-8").read()
    words = len(re.sub(r"<[^>]+>", " ", s).split())
    bad_tags = set(re.findall(r"</?([a-zA-Z0-9]+)", s)) - ALLOWED
    if bad_tags:
        problems.append(f"{slug}: tags not allowed: {sorted(bad_tags)}")
    if re.search(EMPLOYERS, s):
        problems.append(f"{slug}: names an employer in the post body")
    if re.search("[—–]", s):
        problems.append(f"{slug}: contains an em or en dash")
    if not 800 <= words <= 1250:
        problems.append(f"{slug}: {words} words (expected 850 to 1,100)")
    if not s.lstrip().startswith('<p class="lead">'):
        problems.append(f"{slug}: must start with <p class=\"lead\">")
    todo = s.count('class="todo"')
    if todo and slug == strict:
        problems.append(f"{slug}: has {todo} highlighted passage(s); a new post must have none")
    elif todo:
        notes.append(f"{slug}: {todo} highlighted passage(s) still waiting for Atam to vet")
    if f'"slug": "{slug}"' not in open("build.py", encoding="utf-8").read():
        problems.append(f"{slug}: not listed in POSTS in build.py")
    if not os.path.exists(f"blog/{slug}/index.html"):
        problems.append(f"{slug}: page not built (run python3 build.py)")

for n in notes:
    print("note:", n)
if problems:
    print("FAILED")
    for p in problems:
        print(" -", p)
    sys.exit(1)
print("OK")

#!/usr/bin/env python3
"""Decides whether the weekly blog post should be written today.

Prints "POST" or "SKIP: <reason>". One post per ISO week, on a weekday that is
picked pseudo-randomly per week (Monday to Friday). If the chosen day was missed,
the next run that week catches up.
"""
import datetime
import hashlib
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
today = datetime.date.today()
year, week, _ = today.isocalendar()

dates = re.findall(r'"date":\s*"(\d{4}-\d{2}-\d{2})"', (ROOT / "build.py").read_text(encoding="utf-8"))
for d in dates:
    y, w, _ = datetime.date.fromisoformat(d).isocalendar()
    if (y, w) == (year, week):
        print(f"SKIP: a post dated {d} already exists for this week")
        raise SystemExit

chosen = int(hashlib.sha256(f"{year}-W{week}".encode()).hexdigest(), 16) % 5  # 0 = Monday
names = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
if today.weekday() >= chosen:
    print("POST")
else:
    print(f"SKIP: this week's post day is {names[chosen]}")

#!/usr/bin/env python3
"""Regenerates the Progress Overview and Review Queue in README.md from progress.csv.

 Can also append a new attempt directly from the CLI:
    python3 scripts/update_progress.py --log 0217-contains-duplicate \
        --pattern 01-arrays-hashing --difficulty Easy --time 8 \
        --result Solved --cue "Duplicate check in O(n) -> set membership"
"""

from __future__ import annotations

import argparse
import csv
from datetime import date, datetime, timedelta
from pathlib import Path
import re
from urllib.parse import quote

ROOT_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = ROOT_DIR / "progress.csv"
README_PATH = ROOT_DIR / "README.md"

PATTERN_TARGETS: dict[str, int] = {
    "01-arrays-hashing": 9,
    "02-two-pointers": 5,
    "03-sliding-window": 6,
    "04-stack": 7,
    "05-binary-search": 7,
    "06-linked-list": 11,
    "07-trees": 15,
    "08-tries": 3,
    "09-heap": 7,
    "10-backtracking": 9,
    "11-graphs": 19,
    "12-dp": 23,
    "13-greedy": 8,
    "14-intervals": 6,
    "15-bit": 15,
}
TOTAL_TARGET = sum(PATTERN_TARGETS.values())  # 150

REVIEW_OFFSETS_DAYS: dict[str, int] = {
    "Solved": 7,
    "Hinted": 3,
    "Failed": 1,
}


def load_rows() -> list[dict[str, str]]:
    if not CSV_PATH.exists():
        return []
    with CSV_PATH.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        return [row for row in reader if row.get("problem", "").strip()]


def append_attempt(args: argparse.Namespace) -> None:
    rows = load_rows()
    prior_attempts = sum(1 for r in rows if r["problem"] == args.log)
    attempt_num = args.attempts if args.attempts is not None else (prior_attempts + 1)

    solved_date = date.fromisoformat(args.date) if args.date else date.today()
    offset = REVIEW_OFFSETS_DAYS.get(args.result, 7)
    next_rev = (
        args.next_review
        if args.next_review
        else (solved_date + timedelta(days=offset)).isoformat()
    )

    new_row = {
        "problem": args.log,
        "pattern": args.pattern,
        "difficulty": args.difficulty,
        "date": solved_date.isoformat(),
        "time_min": str(args.time),
        "result": args.result,
        "attempts": str(attempt_num),
        "hints_used": args.hints,
        "next_review": next_rev,
        "cue": args.cue,
        "notes": args.notes,
    }

    fieldnames = [
        "problem",
        "pattern",
        "difficulty",
        "date",
        "time_min",
        "result",
        "attempts",
        "hints_used",
        "next_review",
        "cue",
        "notes",
    ]
    file_exists = CSV_PATH.exists() and CSV_PATH.stat().st_size > 0
    with CSV_PATH.open("a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(new_row)


def build_progress_markdown(rows: list[dict[str, str]], ref_date: date | None = None) -> tuple[str, int]:
    solved_by_pattern: dict[str, set[str]] = {p: set() for p in PATTERN_TARGETS}
    attempts_by_pattern: dict[str, int] = {p: 0 for p in PATTERN_TARGETS}
    last_date_by_pattern: dict[str, str] = {p: "—" for p in PATTERN_TARGETS}
    latest_by_problem: dict[str, dict[str, str]] = {}

    for row in rows:
        prob = row["problem"].strip()
        pat = row["pattern"].strip()
        res = row["result"].strip()
        dt = row["date"].strip()

        if pat in attempts_by_pattern:
            attempts_by_pattern[pat] += 1
            if res.lower() == "solved":
                solved_by_pattern[pat].add(prob)
            if last_date_by_pattern[pat] == "—" or dt > last_date_by_pattern[pat]:
                last_date_by_pattern[pat] = dt

        prev = latest_by_problem.get(prob)
        if prev is None or (dt, int(row.get("attempts") or 1)) >= (
            prev["date"].strip(),
            int(prev.get("attempts") or 1),
        ):
            latest_by_problem[prob] = row

    unique_solved = sum(len(s) for s in solved_by_pattern.values())
    total_attempts = len(rows)
    pct = (unique_solved / TOTAL_TARGET) * 100 if TOTAL_TARGET else 0.0

    if ref_date is None:
        dates = []
        for r in rows:
            try:
                dates.append(date.fromisoformat(r["date"].strip()))
            except ValueError:
                pass
        ref_date = max(dates) if dates else date.today()

    horizon = (ref_date + timedelta(days=7)).isoformat()
    due_items = [
        r
        for r in latest_by_problem.values()
        if r.get("next_review", "").strip() and r["next_review"].strip() <= horizon
    ]
    due_items.sort(key=lambda r: (r["next_review"].strip(), r["problem"].strip()))

    lines = [
        "<!-- PROGRESS_START -->",
        "## Progress Overview",
        "",
        "*Auto-generated from [`progress.csv`](progress.csv) via `python3 scripts/update_progress.py`.*",
        "",
        f"- **Unique Problems Solved:** {unique_solved} / {TOTAL_TARGET} ({pct:.1f}%)",
        f"- **Total Attempts Logged:** {total_attempts}",
        "",
        "### By Pattern",
        "",
        "| Pattern | Solved | Target (NC 150) | Attempts | Last Practiced |",
        "| :--- | :---: | :---: | :---: | :---: |",
    ]

    for pat, target in PATTERN_TARGETS.items():
        solved_cnt = len(solved_by_pattern[pat])
        att_cnt = attempts_by_pattern[pat]
        last_dt = last_date_by_pattern[pat]
        lines.append(
            f"| [{pat}](patterns/{pat}/README.md) | {solved_cnt} | {target} | {att_cnt} | {last_dt} |"
        )

    lines.extend(
        [
            "",
            "### Review Queue (Due or Upcoming within 7 Days)",
            "",
            "| Problem | Pattern | Last Result | Next Review | Cue |",
            "| :--- | :--- | :---: | :---: | :--- |",
        ]
    )

    if due_items:
        for item in due_items:
            lines.append(
                f"| `{item['problem']}` | `{item['pattern']}` | {item['result']} | {item['next_review']} | {item['cue']} |"
            )
    else:
        lines.append("| *None due within 7 days* | — | — | — | — |")

    lines.append("<!-- PROGRESS_END -->")
    return "\n".join(lines), unique_solved


def update_readme(rows: list[dict[str, str]]) -> None:
    block, unique_solved = build_progress_markdown(rows)
    content = README_PATH.read_text(encoding="utf-8")

    pattern = re.compile(r"<!-- PROGRESS_START -->.*?<!-- PROGRESS_END -->", re.DOTALL)
    if pattern.search(content):
        content = pattern.sub(block, content)
    else:
        content = content.rstrip() + "\n\n" + block + "\n"

    badge_label = quote(f"{unique_solved} / {TOTAL_TARGET}")
    content = re.sub(
        r"!\[Problems Solved\]\(https://img\.shields\.io/badge/Solved-[^)]+\)",
        f"![Problems Solved](https://img.shields.io/badge/Solved-{badge_label}-2ea44f)",
        content,
    )

    README_PATH.write_text(content, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Update README progress table and optionally log an attempt.")
    parser.add_argument("--log", help="Problem slug to log (e.g., 0217-contains-duplicate)")
    parser.add_argument("--pattern", choices=list(PATTERN_TARGETS.keys()), help="Pattern folder name")
    parser.add_argument("--difficulty", choices=["Easy", "Medium", "Hard"], default="Medium")
    parser.add_argument("--date", help="Date solved (YYYY-MM-DD, defaults to today)")
    parser.add_argument("--time", type=int, default=20, help="Time taken in minutes")
    parser.add_argument("--result", choices=["Solved", "Hinted", "Failed"], default="Solved")
    parser.add_argument("--attempts", type=int, help="Attempt number (auto-incremented if omitted)")
    parser.add_argument("--hints", choices=["No", "Yes"], default="No")
    parser.add_argument("--next-review", help="Next review date (YYYY-MM-DD)")
    parser.add_argument("--cue", default="", help="One-sentence pattern cue")
    parser.add_argument("--notes", default="", help="Short reflection or pitfall note")
    args = parser.parse_args()

    if args.log:
        if not args.pattern or not args.cue:
            parser.error("--pattern and --cue are required when using --log")
        append_attempt(args)

    rows = load_rows()
    update_readme(rows)
    print(f"Updated README.md from progress.csv ({len(rows)} logged attempt(s)).")


if __name__ == "__main__":
    main()

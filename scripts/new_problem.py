#!/usr/bin/env python3
"""Scaffolds a new LeetCode solution file inside the selected pattern folder.

Usage:
    python3 scripts/new_problem.py 217 "Contains Duplicate" \
        --pattern 01-arrays-hashing --difficulty Easy
"""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path
import re

ROOT_DIR = Path(__file__).resolve().parent.parent
PATTERNS_DIR = ROOT_DIR / "patterns"


def slugify(title: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return slug


def camel_case(slug: str) -> str:
    parts = slug.split("-")
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


def main() -> None:
    valid_patterns = sorted(p.name for p in PATTERNS_DIR.iterdir() if p.is_dir())
    parser = argparse.ArgumentParser(description="Create a new LeetCode solution file from the standard header template.")
    parser.add_argument("number", type=int, help="LeetCode problem number (e.g., 217)")
    parser.add_argument("title", help="Problem title (e.g., 'Contains Duplicate')")
    parser.add_argument("--pattern", required=True, choices=valid_patterns, help="Target pattern directory")
    parser.add_argument("--difficulty", choices=["Easy", "Medium", "Hard"], default="Medium")
    parser.add_argument("--cue", default="TODO: Write 1-sentence cue explaining why this pattern applies.")
    args = parser.parse_args()

    num_str = f"{args.number:04d}"
    slug = slugify(args.title)
    func_name = camel_case(slug)
    test_name = f"test_{slug.replace('-', '_')}"
    dest_path = PATTERNS_DIR / args.pattern / f"{num_str}-{slug}.py"

    if dest_path.exists():
        raise SystemExit(f"File already exists: {dest_path}")

    content = f'''"""
Problem: {num_str} - {args.title}
URL: https://leetcode.com/problems/{slug}/
Difficulty: {args.difficulty}
Pattern: {args.pattern}

Cue: {args.cue}
Time Complexity: O(n)
Space Complexity: O(n)

Date Solved: {date.today().isoformat()}
Attempts: 1
Hints Used: No
"""

from typing import List


class Solution:
    def {func_name}(self, nums: List[int]) -> bool:
        raise NotImplementedError


def {test_name}() -> None:
    sol = Solution()
    assert sol is not None
'''
    dest_path.write_text(content, encoding="utf-8")
    print(f"Created {dest_path.relative_to(ROOT_DIR)}")


if __name__ == "__main__":
    main()

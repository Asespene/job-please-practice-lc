# Pattern-First LeetCode & Interview Prep

![Problems Solved](https://img.shields.io/badge/Solved-2%20/%20150-2ea44f)
![Plan](https://img.shields.io/badge/Plan-12--Week%20NeetCode%20150-0969da)
![Language](https://img.shields.io/badge/Language-Python%203-ffd343)

A pattern-first repository for mastering coding interviews (Blind 75 -> NeetCode 150), logging pattern cues, running local tests, and tracking spaced-repetition reviews.

---

## Quick Start: How to Start Your Next Problem

Follow this 3-step loop every time you sit down to solve a problem (e.g., `0217 - Contains Duplicate`):

### Step 1: Scaffold the solution file
```bash
python3 scripts/new_problem.py 217 "Contains Duplicate" \
  --pattern 01-arrays-hashing \
  --difficulty Easy
```
This creates `patterns/01-arrays-hashing/0217-contains-duplicate.py` pre-populated with the standard metadata header, a `Solution` class, and a `test_*()` function. *(Alternatively, copy [`templates/solution_template.py`](templates/solution_template.py) manually).*

### Step 2: Code your solution, fill in the 1-sentence cue & run tests
Open the generated file, write your solution and edge-case assertions, fill in the `Cue:` line in the header, and verify everything passes:
```bash
python3 tests/test_solutions.py
# Or if pytest is installed:
pytest
```

### Step 3: Log your attempt & auto-update the README progress table
Record your attempt in [`progress.csv`](progress.csv) and regenerate the progress dashboard and spaced-repetition review queue below in one command:
```bash
python3 scripts/update_progress.py \
  --log 0217-contains-duplicate \
  --pattern 01-arrays-hashing \
  --difficulty Easy \
  --time 8 \
  --result Solved \
  --cue "Need O(1) duplicate detection -> insert into a set while scanning"
```
*(If you prefer editing [`progress.csv`](progress.csv) by hand, just run `python3 scripts/update_progress.py` afterward to refresh the table).*

---

## Repository Structure

```text
.
├── README.md              # Goals, live progress dashboard, daily workflow
├── PLAN.md                # 12-week schedule (Weeks 1-6 Blind 75, Weeks 7-12 NeetCode 150)
├── progress.csv           # One row per attempt with spaced-repetition next_review dates
├── patterns/              # 15 core patterns with README guides & solution files
│   ├── 01-arrays-hashing/
│   ├── 02-two-pointers/
│   ├── 03-sliding-window/
│   ├── 04-stack/
│   ├── 05-binary-search/
│   ├── 06-linked-list/
│   ├── 07-trees/
│   ├── 08-tries/
│   ├── 09-heap/
│   ├── 10-backtracking/
│   ├── 11-graphs/
│   ├── 12-dp/
│   ├── 13-greedy/
│   ├── 14-intervals/
│   └── 15-bit/
├── templates/             # Reusable Python skeletons (BFS, DFS, Binary Search, DSU, Trie, etc.)
├── notes/                 # Pattern cues, Big-O cheatsheet, personal mistakes log
├── system-design/         # System design framework, checklist, and case studies
├── behavioral/            # STAR story bank & leadership principles grid
├── mocks/                 # Mock interview rubric and session logs
├── scripts/               # Automation for progress tables, review queues, and problem scaffolding
├── tests/                 # Pytest suite that validates every solution and its edge cases
└── .github/workflows/     # CI workflow running pytest and verifying progress tables
```

---

## Standard Solution Header

Every solution file under `patterns/` starts with a concise header so it takes under 30 seconds to fill out:

```python
"""
Problem: 0001 - Two Sum
URL: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Pattern: 01-arrays-hashing

Cue: Need O(1) complement lookup (target - x) while scanning once -> hash map of seen values to indices.
Time Complexity: O(n)
Space Complexity: O(n)

Date Solved: 2026-11-25
Attempts: 1
Hints Used: No
"""
```

---

## Daily Study Workflow

1. **Before coding a new pattern:** Read the pattern's `patterns/<id>/README.md` and the [Tech Interview Handbook cheatsheet](https://www.techinterviewhandbook.org/coding-interview-study-plan/), then watch the overview on [NeetCode](https://neetcode.io/practice).
2. **Timebox your attempt:**
   - **Easy:** 15–20 min
   - **Medium:** 25–30 min
   - **Hard:** 40–45 min
   - *Rule:* Struggle productively first. If stuck at the timebox, read the pattern cue or watch the conceptual explanation—then close the video and code it from scratch.
3. **Write the one-sentence cue:** After solving, write the exact trigger in the solution header and [`notes/pattern-cues.md`](notes/pattern-cues.md).
4. **Log & schedule review:** Record your attempt in [`progress.csv`](progress.csv).
   - **Solved cleanly (`Solved`):** Review in `+7 days` (then `+21 days`).
   - **Needed hint (`Hinted`):** Review in `+3 days` from scratch.
   - **Failed / Timed out (`Failed`):** Review in `+1 to 2 days` from scratch.

---

<!-- PROGRESS_START -->
## Progress Overview

*Auto-generated from [`progress.csv`](progress.csv) via `python3 scripts/update_progress.py`.*

- **Unique Problems Solved:** 2 / 150 (1.3%)
- **Total Attempts Logged:** 2

### By Pattern

| Pattern | Solved | Target (NC 150) | Attempts | Last Practiced |
| :--- | :---: | :---: | :---: | :---: |
| [01-arrays-hashing](patterns/01-arrays-hashing/README.md) | 2 | 9 | 2 | 2026-11-25 |
| [02-two-pointers](patterns/02-two-pointers/README.md) | 0 | 5 | 0 | — |
| [03-sliding-window](patterns/03-sliding-window/README.md) | 0 | 6 | 0 | — |
| [04-stack](patterns/04-stack/README.md) | 0 | 7 | 0 | — |
| [05-binary-search](patterns/05-binary-search/README.md) | 0 | 7 | 0 | — |
| [06-linked-list](patterns/06-linked-list/README.md) | 0 | 11 | 0 | — |
| [07-trees](patterns/07-trees/README.md) | 0 | 15 | 0 | — |
| [08-tries](patterns/08-tries/README.md) | 0 | 3 | 0 | — |
| [09-heap](patterns/09-heap/README.md) | 0 | 7 | 0 | — |
| [10-backtracking](patterns/10-backtracking/README.md) | 0 | 9 | 0 | — |
| [11-graphs](patterns/11-graphs/README.md) | 0 | 19 | 0 | — |
| [12-dp](patterns/12-dp/README.md) | 0 | 23 | 0 | — |
| [13-greedy](patterns/13-greedy/README.md) | 0 | 8 | 0 | — |
| [14-intervals](patterns/14-intervals/README.md) | 0 | 6 | 0 | — |
| [15-bit](patterns/15-bit/README.md) | 0 | 15 | 0 | — |

### Review Queue (Due or Upcoming within 7 Days)

| Problem | Pattern | Last Result | Next Review | Cue |
| :--- | :--- | :---: | :---: | :--- |
| `0001-two-sum` | `01-arrays-hashing` | Solved | 2026-12-02 | Need O(1) complement lookup while iterating once -> hash map value-to-index |
| `0049-group-anagrams` | `01-arrays-hashing` | Solved | 2026-12-02 | Group strings by equivalence under character frequency -> 26-tuple count key in dict |
<!-- PROGRESS_END -->

# 01 - Arrays & Hashing

## Pattern Cues ("If you see X, think Y")
- **Duplicate detection / O(1) membership check:** Use a `set`.
- **Pair / complement lookup (`target - x`):** Use a hash map `val -> index`.
- **Grouping / anagram / equivalence classes:** Map items to a canonical immutable key (`tuple(counts)` or ` "".join(sorted(s))`) in `defaultdict(list)`.
- **Top-K frequent / O(n) frequency sorting:** Count with `Counter`, then use bucket sort (`buckets = [[] for _ in range(n + 1)]`) where index = frequency.
- **Range product / sum without division:** Prefix and suffix passes in $O(n)$ time and $O(1)$ extra space.
- **O(n) consecutive runs:** Insert all into a `set`, and only start counting from `x` if `x - 1 not in num_set`.

## 5-Step Thinking Process
Run through this checklist whenever you encounter an Arrays & Hashing problem:

1. **Check the Constraints ($N$):** If $N \le 10^5$ or $10^6$, $O(n^2)$ will time out—you need $O(n)$ or $O(n \log n)$ (see [`notes/big-o-cheatsheet.md`](../../notes/big-o-cheatsheet.md)).
2. **Name the Brute Force & Spot the Repeated Question:** Ask what a nested inner loop would repeatedly check:
   - *"Have I seen `x` before?"* $\to$ `set`
   - *"Where is the partner `target - x`?"* $\to$ `dict` (`value -> index`)
   - *"How many times does `x` appear?"* $\to$ `Counter` / frequency `dict`
   - *"Which items belong to the same group?"* $\to$ `defaultdict(list)` keyed by a canonical immutable signature (e.g., `tuple(counts)`)
   - *"What are the top $K$ by frequency?"* $\to$ frequency map + bucket array `buckets[freq]`
   - *"What is the product/sum of everything except index `i`?"* $\to$ Prefix pass + Suffix pass
3. **Pick the Lightest Data Structure That Fits:**
   - Only need yes/no existence? $\to$ `set`
   - Need to attach extra data (index, count, group)? $\to$ `dict`
   - Keys come from a tiny fixed range (26 lowercase letters `a–z`, or frequencies `0..n`)? $\to$ plain Python `list`
4. **Decide One-Pass vs. Two-Pass:**
   - **One-pass (on-the-fly):** Check your `set`/`dict` *before* inserting the current element (enables early exit and prevents self-matching; e.g., `Two Sum`, `Contains Duplicate`).
   - **Two-pass (precompute first):** Build the full `set`, frequency map, or prefix array first when you need global knowledge (e.g., `Longest Consecutive Sequence`, `Top K Frequent`, `Product of Array Except Self`).
5. **Quick Edge-Case & Python Sanity Check:**
   - Test empty input (`[]` / `""`), 1 element, all duplicates (`[3, 3, 3]`), negative numbers.
   - Verify all dict keys / set elements are hashable (`tuple`, `str`, `int`—never `list`).
   - State Time and Space complexity separately.

## Core Python Template
```python
from collections import Counter, defaultdict

def bucket_sort_top_k(nums: list[int], k: int) -> list[int]:
    counts = Counter(nums)
    buckets: list[list[int]] = [[] for _ in range(len(nums) + 1)]
    for num, freq in counts.items():
        buckets[freq].append(num)
    res: list[int] = []
    for freq in range(len(buckets) - 1, 0, -1):
        for num in buckets[freq]:
            res.append(num)
            if len(res) == k:
                return res
    return res
```

## Complexity & Pitfalls
- **Time:** Hash table lookup/insert is $O(1)$ average, $O(n)$ worst-case. Sorting keys takes $O(k \log k)$ vs character count tuple $O(k)$.
- **Pitfalls:**
  - Lists and `dict`/`set` are unhashable—convert to `tuple` or `frozenset` before using as dictionary keys.
  - Using `nums[i]` before checking if it refers to the same index in complement lookups (insert into `seen` *after* checking complement).
  - Mutating a dictionary or set while iterating over it.

## Target Problems (NeetCode 150)
- `0217` Contains Duplicate (Easy) *
- `0242` Valid Anagram (Easy) *
- `0001` Two Sum (Easy) *
- `0049` Group Anagrams (Medium) *
- `0347` Top K Frequent Elements (Medium) *
- `0238` Product of Array Except Self (Medium) *
- `0036` Valid Sudoku (Medium)
- `0271` Encode and Decode Strings (Medium) *
- `0128` Longest Consecutive Sequence (Medium) *

*(\* = Blind 75)*

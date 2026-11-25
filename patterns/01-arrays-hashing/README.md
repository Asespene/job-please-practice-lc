# 01 - Arrays & Hashing

## Pattern Cues ("If you see X, think Y")
- **Duplicate detection / O(1) membership check:** Use a `set`.
- **Pair / complement lookup (`target - x`):** Use a hash map `val -> index`.
- **Grouping / anagram / equivalence classes:** Map items to a canonical immutable key (`tuple(counts)` or ` "".join(sorted(s))`) in `defaultdict(list)`.
- **Top-K frequent / O(n) frequency sorting:** Count with `Counter`, then use bucket sort (`buckets = [[] for _ in range(n + 1)]`) where index = frequency.
- **Range product / sum without division:** Prefix and suffix passes in $O(n)$ time and $O(1)$ extra space.
- **O(n) consecutive runs:** Insert all into a `set`, and only start counting from `x` if `x - 1 not in num_set`.

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

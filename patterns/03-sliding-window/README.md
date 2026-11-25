# 03 - Sliding Window

## Pattern Cues ("If you see X, think Y")
- **Longest/shortest contiguous subarray or substring satisfying a constraint:** Expand `r` each step, shrink `l` while the window violates (or satisfies, for minimum window) the invariant.
- **Fixed-size window of length `k`:** Add `s[r]`, remove `s[r - k]` once `r >= k`.
- **Maximum in sliding window of size `k`:** Monotonic decreasing `deque` of indices.

## Core Python Template
```python
def sliding_window_longest(s: str) -> int:
    l = 0
    best = 0
    counts: dict[str, int] = {}
    for r, ch in enumerate(s):
        counts[ch] = counts.get(ch, 0) + 1
        while counts[ch] > 1:  # replace with window-invalid condition
            counts[s[l]] -= 1
            l += 1
        best = max(best, r - l + 1)
    return best
```

## Complexity & Pitfalls
- **Time:** $O(n)$ because `l` and `r` each move forward at most $n$ times ($2n$ operations).
- **Space:** $O(k)$ where $k$ is the alphabet or window size.
- **Pitfalls:**
  - Applying sliding window to subarray sums with **negative numbers** (monotonicity breaks; use prefix sums + hash map or deque instead).
  - Updating `best` before restoring the validity invariant (for longest valid window, update *after* `while invalid`; for shortest valid window, update *inside* `while valid`).

## Target Problems (NeetCode 150)
- `0121` Best Time to Buy and Sell Stock (Easy) *
- `0003` Longest Substring Without Repeating Characters (Medium) *
- `0424` Longest Repeating Character Replacement (Medium) *
- `0567` Permutation in String (Medium)
- `0076` Minimum Window Substring (Hard) *
- `0239` Sliding Window Maximum (Hard)

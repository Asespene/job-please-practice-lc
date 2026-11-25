# 13 - Greedy

## Pattern Cues ("If you see X, think Y")
- **Max contiguous subarray sum (`Maximum Subarray`):** Kadane's algorithm — reset running sum to 0 whenever it drops below 0 (`cur = max(num, cur + num)`).
- **Reachability / minimum jumps (`Jump Game I & II`):** Track the farthest reachable index (`max_reach`) or the BFS-like window `[l, r]` of the current jump level.
- **Circular route feasibility (`Gas Station`):** If `sum(gas) < sum(cost)`, return `-1`; otherwise, whenever running `tank < 0`, reset `start = i + 1` and `tank = 0`.

## Core Python Template
```python
def kadane_max_subarray(nums: list[int]) -> int:
    best = nums[0]
    cur = 0
    for x in nums:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best
```

## Complexity & Pitfalls
- **Time:** Typically $O(n)$ single pass (or $O(n \log n)$ if sorting is required first).
- **Space:** $O(1)$.
- **Pitfalls:**
  - Using greedy when a locally optimal choice doesn't guarantee a global optimum (e.g., general Coin Change requires DP). Always test a quick counterexample before committing to Greedy.

## Target Problems (NeetCode 150)
- `0053` Maximum Subarray (Medium) *
- `0055` Jump Game (Medium) *
- `0045` Jump Game II (Medium)
- `0134` Gas Station (Medium)
- `0846` Hand of Straights (Medium)
- `1899` Merge Triplets to Form Target Triplet (Medium)
- `0763` Partition Labels (Medium)
- `0678` Valid Parenthesis String (Medium)

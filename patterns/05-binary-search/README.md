# 05 - Binary Search

## Pattern Cues ("If you see X, think Y")
- **Sorted array / rotated sorted array in $O(\log n)$:** Binary search on index range.
- **"Minimize the maximum X" or "Find minimum speed/capacity K such that feasible(K) is True":** Binary search on the **answer space** `[lo, hi]` with a monotonic predicate `feasible(mid)`.

## Core Python Template
```python
def binary_search_first_true(lo: int, hi: int, feasible) -> int:
    """Finds the minimum x in [lo, hi] where feasible(x) is True."""
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
```

## Complexity & Pitfalls
- **Time:** $O(\log n)$ for array index search; $O(n \log(\text{max\_val}))$ for binary search on answer space.
- **Space:** $O(1)$.
- **Pitfalls:**
  - Infinite loop when setting `lo = mid` with `mid = (lo + hi) // 2` (if using `lo = mid`, you must use upper mid `(lo + hi + 1) // 2`). Prefer `hi = mid` and `lo = mid + 1`.
  - In rotated sorted arrays, always check which half is sorted first (`if nums[l] <= nums[mid]:` left half is sorted) before checking if `target` lies inside that half.

## Target Problems (NeetCode 150)
- `0704` Binary Search (Easy)
- `0074` Search a 2D Matrix (Medium)
- `0875` Koko Eating Bananas (Medium)
- `0153` Find Minimum in Rotated Sorted Array (Medium) *
- `0033` Search in Rotated Sorted Array (Medium) *
- `0981` Time Based Key-Value Store (Medium)
- `0004` Median of Two Sorted Arrays (Hard)

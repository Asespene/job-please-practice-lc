# 02 - Two Pointers

## Pattern Cues ("If you see X, think Y")
- **Sorted array pair/triplet sum (`Two Sum II`, `3Sum`):** Left pointer at `0`, right pointer at `n - 1`; move `l += 1` if sum is too small, `r -= 1` if too large.
- **Palindrome / symmetric comparison:** Converge `l` and `r` toward the center, skipping non-alphanumeric characters.
- **Container / Trapping Water (bounding height on both sides):** Move the pointer with the smaller boundary inward (`if height[l] < height[r]: l += 1`).

## Core Python Template
```python
def two_pointers_converge(nums: list[int], target: int) -> list[int]:
    l, r = 0, len(nums) - 1
    while l < r:
        cur = nums[l] + nums[r]
        if cur == target:
            return [l, r]
        if cur < target:
            l += 1
        else:
            r -= 1
    return []
```

## Complexity & Pitfalls
- **Time:** $O(n)$ for a single linear pass; $O(n^2)$ for `3Sum` (sort $O(n \log n)$ + outer loop $n \times$ two-pointer pass $n$).
- **Space:** $O(1)$ auxiliary (excluding output and sorting space).
- **Pitfalls:**
  - Forgetting to skip duplicate values in `3Sum` on **both** the outer index `i` (`if i > 0 and nums[i] == nums[i-1]: continue`) and inner pointer `l` after finding a match.
  - Off-by-one between `while l < r` (pair comparison) and `while l <= r` (single-element check).

## Target Problems (NeetCode 150)
- `0125` Valid Palindrome (Easy) *
- `0167` Two Sum II - Input Array Is Sorted (Medium)
- `0015` 3Sum (Medium) *
- `0011` Container With Most Water (Medium) *
- `0042` Trapping Rain Water (Hard)

# 10 - Backtracking

## Pattern Cues ("If you see X, think Y")
- **"Generate all subsets / combinations / permutations / partitions":** Exhaustive search tree with choose -> explore -> unchoose (`path.append(x)` -> `dfs(...)` -> `path.pop()`).
- **Input has duplicates (`Subsets II`, `Combination Sum II`):** Sort the array first, then skip duplicates at the same recursion depth: `if i > start and nums[i] == nums[i - 1]: continue`.
- **2D Grid path existence (`Word Search`) or constraint placement (`N-Queens`):** Mark cell/row/diagonal visited before recursing, and unmark upon returning.

## Core Python Template
```python
def subsets_with_dup(nums: list[int]) -> list[list[int]]:
    nums.sort()
    res: list[list[int]] = []
    path: list[int] = []

    def dfs(start: int) -> None:
        res.append(path.copy())
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            dfs(i + 1)
            path.pop()

    dfs(0)
    return res
```

## Complexity & Pitfalls
- **Time:** Subsets $O(n \cdot 2^n)$; Permutations $O(n \cdot n!)$; Grid search $O(R \cdot C \cdot 3^L)$.
- **Space:** $O(n)$ recursion depth (excluding output list).
- **Pitfalls:**
  - Appending `res.append(path)` instead of `res.append(path.copy())` (all entries in `res` will point to the same mutated list!).
  - Passing `i` instead of `i + 1` when elements **cannot** be reused, or `i + 1` instead of `i` when unlimited reuse **is** allowed (`Combination Sum`).

## Target Problems (NeetCode 150)
- `0078` Subsets (Medium)
- `0039` Combination Sum (Medium) *
- `0046` Permutations (Medium)
- `0090` Subsets II (Medium)
- `0040` Combination Sum II (Medium)
- `0079` Word Search (Medium) *
- `0131` Palindrome Partitioning (Medium)
- `0017` Letter Combinations of a Phone Number (Medium)
- `0051` N-Queens (Hard)

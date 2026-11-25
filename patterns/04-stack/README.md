# 04 - Stack & Monotonic Stack

## Pattern Cues ("If you see X, think Y")
- **Nested matching / balanced delimiters / RPN expression evaluation:** Standard LIFO stack.
- **"Next greater / next smaller element to the right or left":** Monotonic stack storing indices (`while stack and nums[i] > nums[stack[-1]]: idx = stack.pop()`).
- **Largest rectangle / span bounded by smaller bars:** Monotonic increasing stack tracking `(start_index, height)`.

## Core Python Template
```python
def next_greater_elements(nums: list[int]) -> list[int]:
    res = [-1] * len(nums)
    stack: list[int] = []  # stores indices with decreasing values
    for i, val in enumerate(nums):
        while stack and val > nums[stack[-1]]:
            prev_idx = stack.pop()
            res[prev_idx] = i - prev_idx
        stack.append(i)
    return res
```

## Complexity & Pitfalls
- **Time:** $O(n)$ — each index is pushed once and popped at most once.
- **Space:** $O(n)$ for the stack.
- **Pitfalls:**
  - Popping from an empty stack (`if not stack:` check required on closing brackets).
  - Forgetting to process remaining elements left in the monotonic stack after the loop ends (e.g., in `Largest Rectangle in Histogram`).
  - Integer division truncation toward zero in Python: use `int(a / b)` instead of `a // b` for negative numbers (`-3 // 2 == -2`, whereas `int(-3 / 2) == -1`).

## Target Problems (NeetCode 150)
- `0020` Valid Parentheses (Easy) *
- `0155` Min Stack (Medium)
- `0150` Evaluate Reverse Polish Notation (Medium)
- `0022` Generate Parentheses (Medium)
- `0739` Daily Temperatures (Medium)
- `0853` Car Fleet (Medium)
- `0084` Largest Rectangle in Histogram (Hard)

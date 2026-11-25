# 15 - Bit Manipulation & Math / Geometry

## Pattern Cues ("If you see X, think Y")
- **Element appearing once while others appear twice (`Single Number`, `Missing Number`):** XOR cancellation (`x ^ x = 0`, `x ^ 0 = x`).
- **Count set bits (`Number of 1 Bits`):** `n &= (n - 1)` clears the lowest set bit in $O(\text{set bits})$.
- **DP on bit counts (`Counting Bits`):** `dp[i] = dp[i >> 1] + (i & 1)`.
- **In-place 2D matrix rotation (`Rotate Image`):** Transpose across main diagonal (`matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]`), then reverse each row.

## Core Python Template
```python
def hamming_weight(n: int) -> int:
    count = 0
    while n:
        n &= n - 1  # drops lowest set 1-bit
        count += 1
    return count
```

## Complexity & Pitfalls
- **Time:** $O(1)$ (32 iterations for 32-bit integers) or $O(n)$ across an array.
- **Space:** $O(1)$.
- **Pitfalls:**
  - **Python has arbitrary-precision integers** (no automatic 32-bit wrap-around!). In `Sum of Two Integers` (`0371`), apply a 32-bit mask `MASK = 0xFFFFFFFF` each step and check `if a > 0x7FFFFFFF: return ~(a ^ MASK)`.

## Target Problems (NeetCode 150)
- **Bit Manipulation (7):**
  - `0136` Single Number (Easy)
  - `0191` Number of 1 Bits (Easy) *
  - `0338` Counting Bits (Easy) *
  - `0190` Reverse Bits (Easy) *
  - `0268` Missing Number (Easy) *
  - `0371` Sum of Two Integers (Medium) *
  - `0007` Reverse Integer (Medium)
- **Math & Geometry (8):**
  - `0048` Rotate Image (Medium) *
  - `0054` Spiral Matrix (Medium) *
  - `0073` Set Matrix Zeroes (Medium) *
  - `0202` Happy Number (Easy)
  - `0066` Plus One (Easy)
  - `0050` Pow(x, n) (Medium)
  - `0043` Multiply Strings (Medium)
  - `2013` Detect Squares (Medium)

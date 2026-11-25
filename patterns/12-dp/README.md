# 12 - Dynamic Programming (1D & 2D)

## Pattern Cues ("If you see X, think Y")
- **Count ways / min cost / max profit with overlapping subproblems & optimal substructure:** Define state `dp[i]`, transition recurrence, and base cases.
- **Adjacent constraint (`House Robber`):** `dp[i] = max(dp[i-1], dp[i-2] + nums[i])` -> optimize to two variables `prev2, prev1`.
- **0/1 Knapsack (`Partition Equal Subset Sum`, `Target Sum`):** Each item used at most once; iterate capacity **backwards** (or build a new `set`/`dp` row).
- **Unbounded Knapsack (`Coin Change`, `Coin Change II`):** Items can be reused unlimited times; iterate capacity **forwards**.
- **Two strings alignment (`LCS`, `Edit Distance`, `Distinct Subsequences`):** 2D table `dp[i][j]` on prefixes `s1[:i]` and `s2[:j]`.

## Core Python Template
```python
def coin_change(coins: list[int], amount: int) -> int:
    INF = amount + 1
    dp = [0] + [INF] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])
    return dp[amount] if dp[amount] != INF else -1
```

## Complexity & Pitfalls
- **Time:** 1D DP $O(n)$ or $O(n \cdot \text{amount})$; 2D DP $O(m \cdot n)$.
- **Space:** Often reducible from $O(n)$ to $O(1)$, or from $O(m \cdot n)$ to $O(n)$ by keeping only the previous row.
- **Pitfalls:**
  - In `Coin Change II` (counting combinations, not permutations), the outer loop **must** iterate over `coins` and the inner loop over `amount`. Reversing the loops counts permutations!
  - In `Maximum Product Subarray`, you must track both `cur_max` and `cur_min` because a negative number flips the minimum into the maximum.

## Target Problems (NeetCode 150)
- **1D DP (12):** `0070`*, `0746`, `0198`*, `0213`*, `0005`*, `0647`*, `0091`*, `0322`*, `0152`*, `0139`*, `0300`*, `0416`
- **2D DP (11):** `0062`*, `1143`*, `0309`, `0518`, `0494`, `0097`, `0329`, `0115`, `0072`, `0312`, `0010`

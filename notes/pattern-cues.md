# Pattern Cues ("If You See X, Think Y")

After solving each problem, make sure its one-sentence cue is captured here or in the pattern's README. Use this file for **weekend shuffled pattern-recognition drills**.

| If the problem asks for / mentions... | Think of this pattern... | Key Invariant / Trick |
| :--- | :--- | :--- |
| Pair/complement sum or $O(1)$ seen check in unsorted array | **01 - Arrays & Hashing** | Hash map `val -> index` or `set` |
| Group items by anagram / frequency / structural equivalence | **01 - Arrays & Hashing** | Canonical immutable key: `tuple(counts)` in `defaultdict(list)` |
| Top $K$ frequent items in $O(n)$ time | **01 - Arrays & Hashing** | Frequency map + bucket array `buckets[freq]` |
| Consecutive sequence in $O(n)$ without sorting | **01 - Arrays & Hashing** | Only start counting from `x` if `x - 1 not in num_set` |
| Pair/triplet sum in a **sorted** array in $O(1)$ space | **02 - Two Pointers** | Converge `l = 0, r = n - 1`; skip duplicates |
| Longest/shortest **contiguous** subarray/substring with constraint | **03 - Sliding Window** | Expand `r`, shrink `l` while invalid (non-negative values) |
| Maximum/minimum inside a fixed-size sliding window $K$ | **03 - Sliding Window** | Monotonic decreasing `deque` of indices |
| Next greater / next smaller element to the left or right | **04 - Stack** | Monotonic stack storing indices |
| Nested brackets, RPN, or undo-like history | **04 - Stack** | LIFO stack |
| Sorted or rotated sorted array lookup in $O(\log n)$ | **05 - Binary Search** | Identify which half is sorted first |
| "Minimize the maximum X" or monotonic feasibility threshold | **05 - Binary Search** | Binary search on the answer range `[lo, hi]` |
| Cycle detection, middle node, or $O(1)$ space list reorder | **06 - Linked List** | Fast & slow pointers (`slow.next`, `fast.next.next`) |
| $O(1)$ key lookup + $O(1)$ least-recently-used eviction | **06 - Linked List** | Hash map + Doubly Linked List (`LRU Cache`) |
| Subtree height, diameter, balanced check, max path sum | **07 - Trees** | Bottom-up Postorder DFS returning single-branch result |
| Level-by-level tree aggregation or right-side view | **07 - Trees** | BFS queue processing `len(q)` nodes per level |
| Prefix matching (`startsWith`) or multi-word 2D grid search | **08 - Tries** | Prefix Tree (`children` dict + `is_end` flag) |
| $K$-th largest / smallest or stream median | **09 - Heap** | Size-$K$ Min-Heap (or Max-Heap `small` + Min-Heap `large`) |
| Generate **all** subsets, permutations, combinations, or valid placements | **10 - Backtracking** | Choose -> explore -> unchoose (`path.append`, `dfs`, `path.pop`) |
| Shortest path in unweighted graph or multi-source spread | **11 - Graphs** | Multi-source BFS with `deque` |
| Prerequisites, course ordering, or directed cycle detection | **11 - Graphs** | Topological sort (Kahn's in-degree BFS or 3-color DFS) |
| Dynamic connected components or undirected cycle detection | **11 - Graphs** | Union-Find (Disjoint Set Union) |
| Shortest path with non-negative weighted edges | **11 - Graphs** | Dijkstra's algorithm with Min-Heap |
| Count ways / min cost / max profit with choices that depend on prior steps | **12 - Dynamic Programming** | 1D/2D recurrence (Knapsack, sequence alignment, prefix DP) |
| Maximum subarray sum or farthest reachability jump | **13 - Greedy** | Kadane's algorithm or greedy horizon tracking |
| Overlapping time ranges, merging meetings, min rooms | **14 - Intervals** | Sort by `start` (or `end`) time first |
| Single unique number among pairs, bit counting, bitwise addition | **15 - Bit Manipulation** | XOR `a ^ b`, `n &= (n - 1)`, 32-bit mask `0xFFFFFFFF` |

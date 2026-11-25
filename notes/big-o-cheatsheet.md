# Big-O & Python Collections Complexity Cheatsheet

## 1. Input Size ($N$) -> Target Time Complexity

Use the problem constraints to immediately narrow down valid algorithms ($\sim 10^7$–$10^8$ ops/sec limit):

| Constraint on $N$ | Max Acceptable Time | Typical Patterns |
| :--- | :--- | :--- |
| $N \le 10$ | $O(N!)$, $O(2^N)$ | Permutations, Backtracking |
| $N \le 20$ | $O(2^N)$, $O(N \cdot 2^N)$ | Subsets, Bitmask DP, Backtracking |
| $N \le 100$ | $O(N^3)$ | Floyd-Warshall, 3D DP, Interval DP (`Burst Balloons`) |
| $N \le 2,000$ | $O(N^2)$ | 2D DP (`LCS`, `Edit Distance`), `3Sum`, Nested Loops |
| $N \le 10^5$ | $O(N \log N)$ | Sorting, Heap, Binary Search on Answer, Merge Intervals, Dijkstra |
| $N \le 10^6$ | $O(N)$ | Hash Map/Set, Two Pointers, Sliding Window, Monotonic Stack, 1D DP, Greedy |
| $N > 10^8$ | $O(\log N)$ or $O(1)$ | Binary Search, Math / Bit Manipulation |

---

## 2. Python Built-In Data Structures

| Structure | Operation | Average Time | Worst Case | Notes |
| :--- | :--- | :---: | :---: | :--- |
| `list` | `append(x)`, `pop()` | $O(1)$ | $O(1)$ | Dynamic array |
| `list` | `pop(0)`, `insert(0, x)` | $O(n)$ | $O(n)$ | **Never** use `list.pop(0)` for queues; use `collections.deque` |
| `list` | `x in lst` | $O(n)$ | $O(n)$ | Linear scan |
| `list` | `lst.sort()` | $O(n \log n)$ | $O(n \log n)$ | Timsort; $O(n)$ space |
| `collections.deque` | `append`, `appendleft`, `pop`, `popleft` | $O(1)$ | $O(1)$ | Doubly-linked block queue |
| `dict` / `set` | `x in d`, `d[k]`, `add`, `remove` | $O(1)$ | $O(n)$ | Keys must be hashable (`int`, `str`, `tuple`, `frozenset`) |
| `heapq` | `heapify(lst)` | $O(n)$ | $O(n)$ | In-place Min-Heap |
| `heapq` | `heappush`, `heappop`, `heapreplace` | $O(\log n)$ | $O(\log n)$ | `heap[0]` is always the minimum in $O(1)$ |

---

## 3. Graph & Tree Traversals

| Algorithm | Time Complexity | Space Complexity | When to Use |
| :--- | :---: | :---: | :--- |
| **Tree DFS (Pre/In/Post)** | $O(N)$ | $O(H)$ | Height, path sums, BST properties ($H = \log N$ balanced, $N$ skewed) |
| **Tree / Graph BFS** | $O(V + E)$ | $O(V)$ | Level order, shortest path in unweighted graph |
| **Topological Sort** | $O(V + E)$ | $O(V + E)$ | Dependency resolution, cycle detection in DAG |
| **Union-Find (DSU)** | $O(E \cdot \alpha(V))$ | $O(V)$ | Dynamic undirected connectivity, Kruskal's MST |
| **Dijkstra (Min-Heap)** | $O((V + E) \log V)$ | $O(V + E)$ | Shortest path with non-negative edge weights |
| **Bellman-Ford** | $O(V \cdot E)$ | $O(V)$ | Negative weights or at most $K$ stops (`Cheapest Flights Within K Stops`) |
| **Trie** | $O(L)$ per op | $O(N \cdot L)$ | Prefix search, word dictionary on 2D board |

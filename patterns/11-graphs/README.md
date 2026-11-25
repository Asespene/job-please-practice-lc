# 11 - Graphs & Advanced Graphs

## Pattern Cues ("If you see X, think Y")
- **Connected components / flood fill on 2D grid (`Islands`, `Max Area`):** DFS or BFS from each unvisited cell.
- **Shortest path in unweighted graph / simultaneous spread (`Rotting Oranges`, `Walls and Gates`, `Word Ladder`):** Multi-source **BFS** with `deque`.
- **Prerequisites / dependency ordering / cycle detection in directed graph (`Course Schedule`, `Alien Dictionary`):** **Topological Sort** (Kahn's in-degree BFS or 3-state DFS: unvisited/visiting/visited).
- **Dynamic connectivity / cycle in undirected graph (`Redundant Connection`, `Connected Components`):** **Disjoint Set Union (Union-Find)** with path compression and union by rank.
- **Shortest path with non-negative edge weights (`Network Delay Time`, `Swim in Rising Water`):** **Dijkstra's Algorithm** with a Min-Heap.

## Core Python Template
```python
from collections import deque

def topo_sort_kahn(n: int, edges: list[list[int]]) -> list[int]:
    adj: list[list[int]] = [[] for _ in range(n)]
    indegree = [0] * n
    for u, v in edges:
        adj[u].append(v)
        indegree[v] += 1
    q = deque([i for i in range(n) if indegree[i] == 0])
    order: list[int] = []
    while q:
        u = q.popleft()
        order.append(u)
        for nxt in adj[u]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)
    return order if len(order) == n else []
```

## Complexity & Pitfalls
- **Time:** BFS/DFS/Topo Sort $O(V + E)$; Union-Find $O(E \cdot \alpha(V))$; Dijkstra $O((V + E) \log V)$.
- **Pitfalls:**
  - Marking nodes visited when *popping* from BFS queue instead of when *pushing* into the queue (causes duplicate queue entries and TLE).
  - In `Alien Dictionary`, forgetting the invalid prefix edge case where a longer word appears before its own prefix (`"abc"` before `"ab"` -> invalid `""`).

## Target Problems (NeetCode 150)
- `0200` Number of Islands (Medium) *
- `0695` Max Area of Island (Medium)
- `0133` Clone Graph (Medium) *
- `0286` Walls and Gates (Medium)
- `0994` Rotting Oranges (Medium)
- `0417` Pacific Atlantic Water Flow (Medium) *
- `0130` Surrounded Regions (Medium)
- `0207` Course Schedule (Medium) *
- `0210` Course Schedule II (Medium)
- `0261` Graph Valid Tree (Medium) *
- `0323` Number of Connected Components in an Undirected Graph (Medium) *
- `0684` Redundant Connection (Medium)
- `0127` Word Ladder (Hard)
- `0332` Reconstruct Itinerary (Hard)
- `1584` Min Cost to Connect All Points (Medium)
- `0743` Network Delay Time (Medium)
- `0778` Swim in Rising Water (Hard)
- `0269` Alien Dictionary (Hard) *
- `0787` Cheapest Flights Within K Stops (Medium)

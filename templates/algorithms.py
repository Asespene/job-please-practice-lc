"""Reusable Python 3 algorithm skeletons for coding interviews."""

from collections import deque
import heapq
from typing import Callable


# 1. Binary Search (First True / Lower Bound on Answer Space)
def binary_search_first_true(lo: int, hi: int, feasible: Callable[[int], bool]) -> int:
    """Returns the smallest x in [lo, hi] where feasible(x) is True."""
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo


# 2. Sliding Window (Variable Length)
def sliding_window_template(nums: list[int], limit: int) -> int:
    l = 0
    cur_sum = 0
    best = 0
    for r, val in enumerate(nums):
        cur_sum += val
        while cur_sum > limit:
            cur_sum -= nums[l]
            l += 1
        best = max(best, r - l + 1)
    return best


# 3. Monotonic Decreasing Stack (Next Greater Element Indices)
def next_greater_indices(nums: list[int]) -> list[int]:
    res = [-1] * len(nums)
    stack: list[int] = []
    for i, val in enumerate(nums):
        while stack and val > nums[stack[-1]]:
            idx = stack.pop()
            res[idx] = i
        stack.append(i)
    return res


# 4. Grid BFS (Shortest Path in Unweighted 2D Grid)
def grid_bfs(grid: list[list[int]], start: tuple[int, int]) -> list[list[int]]:
    rows, cols = len(grid), len(grid[0])
    dist = [[-1] * cols for _ in range(rows)]
    sr, sc = start
    dist[sr][sc] = 0
    q: deque[tuple[int, int]] = deque([(sr, sc)])
    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

    while q:
        r, c = q.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 0 and dist[nr][nc] == -1:
                dist[nr][nc] = dist[r][c] + 1
                q.append((nr, nc))
    return dist


# 5. Topological Sort (Kahn's In-Degree BFS)
def topological_sort(n: int, edges: list[tuple[int, int]]) -> list[int]:
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


# 6. Disjoint Set Union (Union-Find with Path Compression + Rank)
class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = list(range(n))
        self.rank = [1] * n
        self.components = n

    def find(self, x: int) -> int:
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.rank[ra] += self.rank[rb]
        self.components -= 1
        return True


# 7. Dijkstra's Shortest Path (Non-Negative Weights)
def dijkstra(n: int, edges: list[tuple[int, int, int]], src: int) -> list[int]:
    adj: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((v, w))

    INF = 10**18
    dist = [INF] * n
    dist[src] = 0
    pq: list[tuple[int, int]] = [(0, src)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue
        for v, w in adj[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))
    return dist


# 8. Prefix Tree (Trie)
class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_end: bool = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

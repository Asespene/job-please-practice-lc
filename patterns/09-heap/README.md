# 09 - Heap / Priority Queue

## Pattern Cues ("If you see X, think Y")
- **Top K largest / Kth largest element:** Maintain a **Min-Heap of size $K$** (`heapq`); root `heap[0]` is the $K$-th largest.
- **Top K smallest / K closest points:** Maintain a **Max-Heap of size $K$** by negating values (`-dist`).
- **Running median of a stream:** Two heaps — a Max-Heap `small` (negated values) for the lower half and a Min-Heap `large` for the upper half, kept balanced within size 1.
- **Cooldown scheduling (`Task Scheduler`):** Max-Heap of remaining frequencies + FIFO `deque` of `(remaining_count, available_time)`.

## Core Python Template
```python
import heapq

def kth_largest(nums: list[int], k: int) -> int:
    min_heap = nums[:k]
    heapq.heapify(min_heap)
    for num in nums[k:]:
        if num > min_heap[0]:
            heapq.heapreplace(min_heap, num)
    return min_heap[0]
```

## Complexity & Pitfalls
- **Time:** `heapify` is $O(n)$; `heappush`/`heappop` on size-$k$ heap is $O(\log k)$. Building top-$k$ takes $O(n \log k)$.
- **Space:** $O(k)$ for the heap.
- **Pitfalls:**
  - Python's `heapq` is a **Min-Heap only**—remember to negate numeric priorities (`-val`) for a Max-Heap, and negate again when popping.
  - When pushing tuples `(priority, item)` where `item` is not comparable (like `ListNode`), include a tie-breaker index `(priority, i, item)`.

## Target Problems (NeetCode 150)
- `0703` Kth Largest Element in a Stream (Easy)
- `1046` Last Stone Weight (Easy)
- `0973` K Closest Points to Origin (Medium)
- `0215` Kth Largest Element in an Array (Medium)
- `0621` Task Scheduler (Medium)
- `0355` Design Twitter (Medium)
- `0295` Find Median from Data Stream (Hard) *

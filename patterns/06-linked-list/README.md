# 06 - Linked List

## Pattern Cues ("If you see X, think Y")
- **Middle of list / cycle detection / cycle entry:** Fast and slow pointers (`slow = slow.next`, `fast = fast.next.next`).
- **Nth node from end:** Advance `fast` by `n` steps first, then move `slow` and `fast` together until `fast` hits end.
- **Head might change (deletion, merge, reversal in groups):** Create a `dummy = ListNode(0, head)` and return `dummy.next`.
- **O(1) key lookup + O(1) recency update (`LRU Cache`):** Hash map + Doubly Linked List with sentinel `left` (LRU) and `right` (MRU) nodes.

## Core Python Template
```python
class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next

def reverse_list(head: ListNode | None) -> ListNode | None:
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
```

## Complexity & Pitfalls
- **Time:** $O(n)$ traversal; **Space:** $O(1)$ in-place pointer manipulation.
- **Pitfalls:**
  - Losing the reference to `curr.next` before reassigning `curr.next = prev`.
  - Not terminating the first half of a split list (`slow.next = None`), causing cycles during merge (`Reorder List`).

## Target Problems (NeetCode 150)
- `0206` Reverse Linked List (Easy) *
- `0021` Merge Two Sorted Lists (Easy) *
- `0141` Linked List Cycle (Easy) *
- `0143` Reorder List (Medium) *
- `0019` Remove Nth Node From End of List (Medium) *
- `0138` Copy List with Random Pointer (Medium)
- `0002` Add Two Numbers (Medium)
- `0287` Find the Duplicate Number (Medium)
- `0146` LRU Cache (Medium)
- `0023` Merge k Sorted Lists (Hard) *
- `0025` Reverse Nodes in k-Group (Hard)

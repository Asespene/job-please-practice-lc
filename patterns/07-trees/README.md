# 07 - Trees (Binary Trees & BSTs)

## Pattern Cues ("If you see X, think Y")
- **Height, diameter, balanced check, max path sum:** Bottom-up **Postorder DFS** (compute left and right children first, update global answer, return single-branch value to parent).
- **Path constraint from root (Good Nodes, Validate BST with `(low, high)` bounds):** Top-down **Preorder DFS** passing state down.
- **Level-by-level / right side view / minimum depth:** **BFS** using `collections.deque` with `for _ in range(len(q)):`.
- **Sorted order in a BST (`Kth Smallest`, `Validate BST`):** **Inorder DFS** visits BST nodes in non-decreasing order.

## Core Python Template
```python
from collections import deque

class TreeNode:
    def __init__(self, val: int = 0, left: "TreeNode | None" = None, right: "TreeNode | None" = None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root: TreeNode | None) -> list[list[int]]:
    if not root:
        return []
    res: list[list[int]] = []
    q = deque([root])
    while q:
        level = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        res.append(level)
    return res
```

## Complexity & Pitfalls
- **Time:** $O(n)$ visiting every node once.
- **Space:** $O(h)$ recursion stack for DFS ($O(\log n)$ balanced, $O(n)$ skewed); $O(w)$ queue width for BFS.
- **Pitfalls:**
  - Checking only `node.left.val < node.val < node.right.val` in `Validate BST` instead of enforcing full ancestor bounds `(low < node.val < high)`.
  - Returning the two-branch split sum instead of the single-branch max in `Binary Tree Maximum Path Sum`.

## Target Problems (NeetCode 150)
- `0226` Invert Binary Tree (Easy) *
- `0104` Maximum Depth of Binary Tree (Easy) *
- `0543` Diameter of Binary Tree (Easy)
- `0110` Balanced Binary Tree (Easy)
- `0100` Same Tree (Easy) *
- `0572` Subtree of Another Tree (Easy) *
- `0235` Lowest Common Ancestor of a Binary Search Tree (Medium) *
- `0102` Binary Tree Level Order Traversal (Medium) *
- `0199` Binary Tree Right Side View (Medium)
- `1448` Count Good Nodes in Binary Tree (Medium)
- `0098` Validate Binary Search Tree (Medium) *
- `0230` Kth Smallest Element in a BST (Medium) *
- `0105` Construct Binary Tree from Preorder and Inorder Traversal (Medium) *
- `0124` Binary Tree Maximum Path Sum (Hard) *
- `0297` Serialize and Deserialize Binary Tree (Hard) *

# 08 - Tries (Prefix Trees)

## Pattern Cues ("If you see X, think Y")
- **Prefix matching (`startsWith`), autocomplete, dictionary word lookup:** Trie where each node has `children: dict[str, TrieNode]` and `is_end: bool`.
- **Wildcard search (`.` matches any char):** Trie + DFS branching over all `node.children.values()` when seeing `.`.
- **Simultaneous multi-word search on a 2D board (`Word Search II`):** Insert all words into a Trie, then run grid DFS guided by the Trie (prune matched words to avoid re-visiting).

## Core Python Template
```python
class TrieNode:
    def __init__(self) -> None:
        self.children: dict[str, TrieNode] = {}
        self.is_end: bool = False

class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.is_end = True
```

## Complexity & Pitfalls
- **Time:** $O(L)$ per `insert`, `search`, or `startsWith` where $L$ is word length.
- **Space:** $O(N \cdot L)$ total characters across all inserted words.
- **Pitfalls:**
  - Returning `True` on `search(word)` without checking `curr.is_end` (matching a prefix instead of a complete word).
  - TLE on `Word Search II` if you don't prune leaf nodes or clear `node.word = None` once a word is collected.

## Target Problems (NeetCode 150)
- `0208` Implement Trie (Prefix Tree) (Medium) *
- `0211` Design Add and Search Words Data Structure (Medium) *
- `0212` Word Search II (Hard) *

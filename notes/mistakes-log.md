# Personal Mistakes & Bug Log

Log every bug, misread constraint, off-by-one error, or missed edge case you encounter during practice. Review this file for 5 minutes before every mock interview.

---

## Common Python & Algorithmic Traps Checklist

- [ ] **Shallow copy in Backtracking:** Did I write `res.append(path.copy())` instead of `res.append(path)`?
- [ ] **2D Matrix initialization:** Did I write `[[0] * cols for _ in range(rows)]` instead of `[[0] * cols] * rows` (which aliases rows)?
- [ ] **BFS visited timing:** Did I mark `(nr, nc)` as visited **before** pushing to `deque` rather than after popping?
- [ ] **Negative division toward zero:** Did I use `int(a / b)` instead of `a // b` when truncating negative quotients toward zero (e.g., `Evaluate Reverse Polish Notation`)?
- [ ] **Heapq sign inversion:** Did I negate values (`-x`) when using `heapq` as a Max-Heap, and negate again when reading/popping?
- [ ] **Tree BST validation:** Did I pass `(low, high)` ancestor bounds down the recursion instead of only checking immediate children?
- [ ] **Edge cases checked:** Empty input `[]` / `""`, single element `[x]`, all duplicates `[3, 3, 3]`, all negative numbers `[-5, -2, -9]`, skewed tree (linked list), disconnected graph.

---

## Session Mistake Log

| Date | Problem | Pattern | What Went Wrong (Bug / Misread / Bottleneck) | Fix / Rule for Next Time |
| :--- | :--- | :--- | :--- | :--- |
| 2026-11-25 | `0001-two-sum` | `01-arrays-hashing` | (Example) If you populate the full dict before scanning, `[3, 3]` with target `6` can overwrite index `0` | Check `target - num in seen` first, then set `seen[num] = i` in a single pass |
| 2026-11-25 | `0049-group-anagrams` | `01-arrays-hashing` | (Example) Lists cannot be dict keys (`TypeError: unhashable type: 'list'`) | Convert 26-char frequency `list` to `tuple(counts)` before indexing `defaultdict(list)` |
| 2026-11-26 | `0217-contains-duplicate` | `01-arrays-hashing` | Checked/added index `i` instead of value `nums[i]` inside `for i in range(len(nums))` | Prefer `for num in nums:` when index isn't needed; otherwise always index `nums[i]` |

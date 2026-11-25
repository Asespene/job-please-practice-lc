# Mock Interviews Guide & Log

Rehearsing out loud is a separate skill from solving problems silently. Schedule **one mock interview per week** starting in Week 2 (via Pramp, interviewing.io, a peer, or a recorded solo timer session).

---

## The 6-Step Technical Interview Checklist (UMPIRE)

Use this exact sequence on every mock and real interview:

1. **U — Understand & Clarify (2–3 min):**
   - Restate the problem in your own words.
   - Ask about input types, size bounds ($N$), negative numbers, duplicates, empty inputs, graph cycles/disconnects, and whether in-place mutation is allowed.
2. **M — Match Pattern & Compare Trade-offs (3–5 min):**
   - State the brute-force approach and its Big-O in 1–2 sentences.
   - Propose the optimal pattern (e.g., "Because we need the longest valid contiguous substring, we can use a variable-length sliding window in $O(n)$ time and $O(k)$ space").
   - Get explicit buy-in from the interviewer before writing code.
3. **P — Plan / Pseudocode (2–3 min):**
   - Write 3–5 bullet comments outlining the state variables and loop invariant.
4. **I — Implement Cleanly (15–20 min):**
   - Use meaningful variable names, helper functions, and standard Python idioms (`enumerate`, `collections.deque`, `defaultdict`).
   - Narrate your high-level intent as you code rather than reading syntax character-by-character.
5. **R — Review & Dry-Run by Hand (5 min):**
   - Trace through a small non-trivial example line-by-line, tracking variable states in a comment table.
   - Check edge cases (`[]`, single element, duplicates, off-by-one bounds).
6. **E — Evaluate Complexity (1–2 min):**
   - State tight Time and Space complexity (including recursion stack and output allocations).

---

## Mock Interview Session Log

| Session # | Date | Platform / Partner | Problems Covered | Score (1–4) | Key Takeaway / Action Item |
| :---: | :--- | :--- | :--- | :---: | :--- |
| 0 | 2026-11-25 | Solo Timer Template | [`00-mock-template.md`](00-mock-template.md) | — | Template for weekly mock logs |

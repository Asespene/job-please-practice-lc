# 12-Week Study & Rollout Plan (Blind 75 -> NeetCode 150)

This schedule implements a **pattern-first**, **spaced-repetition** progression in Python 3:
- **Weeks 1–6:** Complete the **Blind 75** core by pattern (2–3 problems/day).
- **Weeks 7–12:** Expand to the full **NeetCode 150**, filling in Tries, Intervals, Bit Manipulation, Advanced Graphs, 2D DP, and Greedy, plus interleaved sets and company-specific sprints.

---

## Weekly Cadence & Quota

Aim for **~6–8 hours/week** split across high-focus blocks:
- **3x 60-minute New Problem Sessions:** 2–3 problems from the current pattern.
- **2x 45-minute Spaced Review Sessions:** Re-solve problems from [`progress.csv`](progress.csv) whose `next_review` date has arrived—from scratch, without looking at previous code.
- **1x 90-minute Interleaved / Mock Session (Weekends):**
  - *Part 1 (20 min):* Pattern Recognition Drill—pick 5 random problems and write down **only the pattern and 1-sentence cue** without coding.
  - *Part 2 (45 min):* Timed mock interview (out loud or via Pramp / peer) logged in [`mocks/`](mocks/).
  - *Part 3 (25 min):* Retro in [`notes/mistakes-log.md`](notes/mistakes-log.md).

---

## Phase 0: Setup & Workflow Calibration (Day 0)

- [x] Verify `pytest` and `python3 scripts/update_progress.py` work locally.
- [x] Review [`templates/algorithms.py`](templates/algorithms.py) and [`notes/big-o-cheatsheet.md`](notes/big-o-cheatsheet.md).
- [x] Study two starter solutions in [`patterns/01-arrays-hashing/`](patterns/01-arrays-hashing/).

---

## Phase 1: Blind 75 Core by Pattern (Weeks 1–6)

### Week 1: Arrays & Hashing + Two Pointers (12 problems)
- **01-arrays-hashing (8):**
  - [x] `0001` Two Sum (Easy)
  - [ ] `0217` Contains Duplicate (Easy)
  - [ ] `0242` Valid Anagram (Easy)
  - [x] `0049` Group Anagrams (Medium)
  - [ ] `0347` Top K Frequent Elements (Medium)
  - [ ] `0238` Product of Array Except Self (Medium)
  - [ ] `0271` Encode and Decode Strings (Medium)
  - [ ] `0128` Longest Consecutive Sequence (Medium)
- **02-two-pointers (3):**
  - [ ] `0125` Valid Palindrome (Easy)
  - [ ] `0015` 3Sum (Medium)
  - [ ] `0011` Container With Most Water (Medium)

### Week 2: Sliding Window + Stack + Binary Search (8 problems)
- **03-sliding-window (4):**
  - [ ] `0121` Best Time to Buy and Sell Stock (Easy)
  - [ ] `0003` Longest Substring Without Repeating Characters (Medium)
  - [ ] `0424` Longest Repeating Character Replacement (Medium)
  - [ ] `0076` Minimum Window Substring (Hard)
- **04-stack (1):**
  - [ ] `0020` Valid Parentheses (Easy)
- **05-binary-search (2):**
  - [ ] `0153` Find Minimum in Rotated Sorted Array (Medium)
  - [ ] `0033` Search in Rotated Sorted Array (Medium)

### Week 3: Linked List + Trees Part 1 (13 problems)
- **06-linked-list (6):**
  - [ ] `0206` Reverse Linked List (Easy)
  - [ ] `0021` Merge Two Sorted Lists (Easy)
  - [ ] `0141` Linked List Cycle (Easy)
  - [ ] `0143` Reorder List (Medium)
  - [ ] `0019` Remove Nth Node From End of List (Medium)
  - [ ] `0023` Merge k Sorted Lists (Hard)
- **07-trees Part 1 (7):**
  - [ ] `0226` Invert Binary Tree (Easy)
  - [ ] `0104` Maximum Depth of Binary Tree (Easy)
  - [ ] `0100` Same Tree (Easy)
  - [ ] `0572` Subtree of Another Tree (Easy)
  - [ ] `0235` Lowest Common Ancestor of a Binary Search Tree (Medium)
  - [ ] `0102` Binary Tree Level Order Traversal (Medium)
  - [ ] `0098` Validate Binary Search Tree (Medium)

### Week 4: Trees Part 2 + Tries + Heap + Backtracking (11 problems)
- **07-trees Part 2 (4):**
  - [ ] `0230` Kth Smallest Element in a BST (Medium)
  - [ ] `0105` Construct Binary Tree from Preorder and Inorder Traversal (Medium)
  - [ ] `0124` Binary Tree Maximum Path Sum (Hard)
  - [ ] `0297` Serialize and Deserialize Binary Tree (Hard)
- **08-tries (3):**
  - [ ] `0208` Implement Trie (Prefix Tree) (Medium)
  - [ ] `0211` Design Add and Search Words Data Structure (Medium)
  - [ ] `0212` Word Search II (Hard)
- **09-heap (1):**
  - [ ] `0295` Find Median from Data Stream (Hard)
- **10-backtracking (2):**
  - [ ] `0039` Combination Sum (Medium)
  - [ ] `0079` Word Search (Medium)

### Week 5: Graphs + 1D Dynamic Programming (16 problems)
- **11-graphs (7):**
  - [ ] `0200` Number of Islands (Medium)
  - [ ] `0133` Clone Graph (Medium)
  - [ ] `0417` Pacific Atlantic Water Flow (Medium)
  - [ ] `0207` Course Schedule (Medium)
  - [ ] `0323` Number of Connected Components in an Undirected Graph (Medium)
  - [ ] `0261` Graph Valid Tree (Medium)
  - [ ] `0269` Alien Dictionary (Hard)
- **12-dp (1D Core - 10):**
  - [ ] `0070` Climbing Stairs (Easy)
  - [ ] `0198` House Robber (Medium)
  - [ ] `0213` House Robber II (Medium)
  - [ ] `0005` Longest Palindromic Substring (Medium)
  - [ ] `0647` Palindromic Substrings (Medium)
  - [ ] `0091` Decode Ways (Medium)
  - [ ] `0322` Coin Change (Medium)
  - [ ] `0152` Maximum Product Subarray (Medium)
  - [ ] `0139` Word Break (Medium)
  - [ ] `0300` Longest Increasing Subsequence (Medium)

### Week 6: 2D DP + Greedy + Intervals + Bit Manipulation (15 problems — Blind 75 Complete!)
- **12-dp (2D Core - 2):**
  - [ ] `0062` Unique Paths (Medium)
  - [ ] `1143` Longest Common Subsequence (Medium)
- **13-greedy (2):**
  - [ ] `0053` Maximum Subarray (Medium)
  - [ ] `0055` Jump Game (Medium)
- **14-intervals (5):**
  - [ ] `0057` Insert Interval (Medium)
  - [ ] `0056` Merge Intervals (Medium)
  - [ ] `0435` Non-overlapping Intervals (Medium)
  - [ ] `0252` Meeting Rooms (Easy)
  - [ ] `0253` Meeting Rooms II (Medium)
- **15-bit (6):**
  - [ ] `0191` Number of 1 Bits (Easy)
  - [ ] `0338` Counting Bits (Easy)
  - [ ] `0190` Reverse Bits (Easy)
  - [ ] `0268` Missing Number (Easy)
  - [ ] `0371` Sum of Two Integers (Medium)
  - [ ] `0048` Rotate Image / `0054` Spiral Matrix / `0073` Set Matrix Zeroes (Math & Geometry core)

---

## Phase 2: NeetCode 150 Expansion & Interleaving (Weeks 7–12)

### Week 7: Monotonic Stack, Advanced Binary Search & Sliding Window Expansion (14 problems)
- **01-arrays-hashing:** `0036` Valid Sudoku
- **02-two-pointers:** `0167` Two Sum II, `0042` Trapping Rain Water
- **03-sliding-window:** `0567` Permutation in String, `0239` Sliding Window Maximum
- **04-stack:** `0155` Min Stack, `0150` Evaluate Reverse Polish Notation, `0022` Generate Parentheses, `0739` Daily Temperatures, `0853` Car Fleet, `0084` Largest Rectangle in Histogram
- **05-binary-search:** `0704` Binary Search, `0074` Search a 2D Matrix, `0875` Koko Eating Bananas, `0981` Time Based Key-Value Store, `0004` Median of Two Sorted Arrays

### Week 8: Linked Lists, Trees & Heap / Priority Queue Expansion (15 problems)
- **06-linked-list:** `0138` Copy List with Random Pointer, `0002` Add Two Numbers, `0287` Find the Duplicate Number, `0146` LRU Cache, `0025` Reverse Nodes in k-Group
- **07-trees:** `0543` Diameter of Binary Tree, `0110` Balanced Binary Tree, `0199` Binary Tree Right Side View, `1448` Count Good Nodes in Binary Tree
- **09-heap:** `0703` Kth Largest Element in a Stream, `1046` Last Stone Weight, `0973` K Closest Points to Origin, `0215` Kth Largest Element in an Array, `0621` Task Scheduler, `0355` Design Twitter

### Week 9: Complete Backtracking & Graph Algorithms (19 problems)
- **10-backtracking (7):**
  - `0078` Subsets, `0046` Permutations, `0090` Subsets II, `0040` Combination Sum II, `0131` Palindrome Partitioning, `0017` Letter Combinations of a Phone Number, `0051` N-Queens
- **11-graphs & Advanced Graphs (12):**
  - `0695` Max Area of Island, `0130` Surrounded Regions, `0994` Rotting Oranges, `0286` Walls and Gates, `0210` Course Schedule II, `0684` Redundant Connection, `0127` Word Ladder
  - *Advanced Graphs:* `0332` Reconstruct Itinerary, `1584` Min Cost to Connect All Points, `0743` Network Delay Time, `0778` Swim in Rising Water, `0787` Cheapest Flights Within K Stops

### Week 10: 1D & 2D Dynamic Programming Mastery (11 problems)
- **12-dp (1D remaining):** `0746` Min Cost Climbing Stairs, `0416` Partition Equal Subset Sum
- **12-dp (2D remaining):** `0309` Best Time to Buy and Sell Stock with Cooldown, `0518` Coin Change II, `0494` Target Sum, `0097` Interleaving String, `0329` Longest Increasing Path in a Matrix, `0115` Distinct Subsequences, `0072` Edit Distance, `0312` Burst Balloons, `0010` Regular Expression Matching

### Week 11: Greedy, Intervals, Bit & Math Expansion + System Design & Behavioral (16 problems)
- **13-greedy:** `0045` Jump Game II, `0846` Hand of Straights, `1899` Merge Triplets to Form Target Triplet, `0763` Partition Labels, `0678` Valid Parenthesis String, `0134` Gas Station
- **14-intervals:** `1851` Minimum Interval to Include Each Query
- **15-bit & Math:** `0136` Single Number, `0007` Reverse Integer, `0202` Happy Number, `0066` Plus One, `0050` Pow(x, n), `0043` Multiply Strings, `2013` Detect Squares
- **Non-Coding Prep:** Finalize 6 core stories in [`behavioral/star-stories.md`](behavioral/star-stories.md) and review [`system-design/README.md`](system-design/README.md).

### Week 12: Shuffled Interleaving, Company Sprints & Timed Mocks
- **Interleaved Sets:** Do 3 timed 60-minute blocks of 2 random Mediums without knowing the pattern beforehand.
- **Spaced-Repetition Clearout:** Clear every overdue problem in [`progress.csv`](progress.csv).
- **Company-Tagged Filter:** Use public company problem lists for your target company during the final 7–10 days.
- **2 Full Mock Loops:** 45-min coding + 15-min behavioral logged in [`mocks/`](mocks/).

---

## Alternative Compressed Tracks

- **4-Week Sprint:** Do Weeks 1–5 (skipping Hard problems except `0076`, `0023`, `0124`, `0295`) + `0056` Merge Intervals + `0208` Implement Trie.
- **6-Week Blind 75 Track:** Follow Weeks 1–6 above at 2 problems/Weekday + 3 review problems/Weekend.

---

## Essential External References

- **Problem Lists:**
  - [NeetCode 150 Practice Tracker](https://neetcode.io/practice)
  - [Grind 75 Adaptive Schedule Generator](https://www.techinterviewhandbook.org/grind75/)
- **Cheatsheets & Guides:**
  - [Tech Interview Handbook Algorithm Cheatsheets](https://www.techinterviewhandbook.org/coding-interview-study-plan/)
  - [System Design Primer (GitHub)](https://github.com/donnemartin/system-design-primer)
- **Company-Wise Question Lists (Use in Weeks 11–12 only):**
  - [hxu296/leetcode-company-wise-problems-2022](https://github.com/hxu296/leetcode-company-wise-problems-2022)
  - [liquidslr/leetcode-company-wise-problems](https://github.com/liquidslr/leetcode-company-wise-problems)
- **Mock Platforms:**
  - [Pramp (Peer Mocks)](https://www.pramp.com/)
  - [interviewing.io](https://interviewing.io/)

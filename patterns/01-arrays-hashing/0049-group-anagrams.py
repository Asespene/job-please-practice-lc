"""
Problem: 0049 - Group Anagrams
URL: https://leetcode.com/problems/group-anagrams/
Difficulty: Medium
Pattern: 01-arrays-hashing

Cue: Group strings by character-frequency equivalence -> use a 26-element count tuple as a dictionary key.
Time Complexity: O(n * k) where n = len(strs) and k = max string length
Space Complexity: O(n * k)

Date Solved: 2026-11-25
Attempts: 1
Hints Used: No
"""

from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups: dict[tuple[int, ...], List[str]] = defaultdict(list)
        for s in strs:
            counts = [0] * 26
            for ch in s:
                counts[ord(ch) - ord("a")] += 1
            groups[tuple(counts)].append(s)
        return list(groups.values())


def _normalize(groups: List[List[str]]) -> List[List[str]]:
    return sorted(sorted(g) for g in groups)


def test_group_anagrams() -> None:
    sol = Solution()
    assert _normalize(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) == _normalize(
        [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    )
    assert sol.groupAnagrams([""]) == [[""]]
    assert sol.groupAnagrams(["a"]) == [["a"]]

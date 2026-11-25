"""
Problem: 0000 - Problem Title
URL: https://leetcode.com/problems/problem-slug/
Difficulty: Easy | Medium | Hard
Pattern: 01-arrays-hashing

Cue: One sentence naming the signal in the problem that pointed to this pattern.
Time Complexity: O(n)
Space Complexity: O(n)

Date Solved: YYYY-MM-DD
Attempts: 1
Hints Used: No
"""

from typing import List


class Solution:
    def solve(self, nums: List[int]) -> int:
        return len(nums)


def test_solve() -> None:
    sol = Solution()
    assert sol.solve([1, 2, 3]) == 3
    assert sol.solve([]) == 0

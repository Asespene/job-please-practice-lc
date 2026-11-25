"""
Problem: 0001 - Two Sum
URL: https://leetcode.com/problems/two-sum/
Difficulty: Easy
Pattern: 01-arrays-hashing

Cue: Need O(1) complement lookup (target - x) while scanning once -> hash map of seen values to indices.
Time Complexity: O(n)
Space Complexity: O(n)

Date Solved: 2026-11-25
Attempts: 1
Hints Used: No
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: dict[int, int] = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []


def test_two_sum() -> None:
    sol = Solution()
    assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert sol.twoSum([3, 2, 4], 6) == [1, 2]
    assert sol.twoSum([3, 3], 6) == [0, 1]
    assert sol.twoSum([-3, 4, 3, 90], 0) == [0, 2]

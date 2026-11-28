"""
Problem: 0217 - Contains Duplicate
URL: https://leetcode.com/problems/contains-duplicate/
Difficulty: Easy
Pattern: 01-arrays-hashing

Cue: Need O(1) duplicate detection while scanning once -> check and insert into a set.
Time Complexity: O(n)
Space Complexity: O(n)

Date Solved: 2026-11-26
Attempts: 1
Hints Used: No
"""

from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #typically we can just brute force and check each values in a nested loop if any of them are the same then return true
        #brute force, compare the outer loop element with each element using the inner loop
        #ways to improve this bruteforce is by using a dict/set or cutting elements we need to check as we linearly passes meaning the condition filters out stuff

        #the inner loop is checking if we've seen element x in the list ---> sets

        #empty set to place elements we have already seen
        seen = set()

        for i in range(len(nums)):
            #iterate through our list as we iterate we add each element, add to the set.
            #set only stores unique elements
            if (nums[i] in seen):
                return True

            seen.add(nums[i])

        return False

        #thought process
        #finding duplicates is basically just comparing 2 values and ensuring that they match.
        #this is too slow since we are looping through n x n elements. So we can just loop through once and as we loop through once store first seen element
        #then if we check if the element we've already seen is the the element we are looping over. Do this until we looped through the entire list ensuring that we find a duplicate since we store each seen element.
        #set just works out in this question since the core idea of that ds is that it stores unique elements and no duplicate so by using that as check reference we ensure that a new element we are looping has to be first seen or we've already seen it
        #using ds ensures our space is O(n)


        
    #brute force method
    """
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if (i == j):
                return True

        return False

    """

    #with the bruteforce method our complexity is O(n^2) where time is n^2 since we have a nested loop where we loop through the array twice whereas our space complexity is constant time since we are using the given container or just list
def test_contains_duplicate() -> None:
    sol = Solution()
    assert sol.containsDuplicate([1, 2, 3, 1]) is True
    assert sol.containsDuplicate([1, 2, 3, 4]) is False
    assert sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    assert sol.containsDuplicate([]) is False
    assert sol.containsDuplicate([42]) is False
    assert sol.containsDuplicate([-1, -2, -1]) is True

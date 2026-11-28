"""
Problem: 0242 - Valid Anagram
URL: https://leetcode.com/problems/valid-anagram/
Difficulty: Easy
Pattern: 01-arrays-hashing

Cue: Need to verify two strings have identical character frequencies -> count chars in each string with hash maps and compare.
Time Complexity: O(n)
Space Complexity: O(k) where k <= 26 unique characters (O(1) for lowercase English)

Date Solved: 2026-11-27
Attempts: 1
Hints Used: Yes
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #given 2 strings, return if the two string is an anagram

        #what is an anagram
        #criteria
        #same length in amount of letters
        #same count of letters, each letter shows up the same amount of time.


        if len(s) != len(t):
            return False

        #dictionaries
        #count how many times each char shows up in both strings
        s_count = {}
        t_count = {}

        #loop through one of the string for the count, if the element is in the string store it in their respective dict. If they are the same by the end of the loop they are an anagram
        for i in s:
            #if already inside then just increment otherwise set to 1
            if i in s_count:
                s_count[i] += 1
            else:
                s_count[i] = 1

        for j in t:
            if j in t_count:
                t_count[j] += 1
            else:
                t_count[j] = 1

        if (s_count == t_count):
            return True

        return False

        #cue
        #the time compelxity of this would n since we are using one for loop of n lements across the string
        #the space compelexity would also be n since we are using a dictionary as a way to check if each string have the same number of elements. We use 2 so there is 2n space complexity
        #as a whole this is a O(n) implementation.

        #othe


def test_valid_anagram() -> None:
    sol = Solution()
    assert sol.isAnagram("anagram", "nagaram") is True
    assert sol.isAnagram("rat", "car") is False
    assert sol.isAnagram("aab", "abb") is False
    assert sol.isAnagram("aacc", "ccac") is False
    assert sol.isAnagram("", "") is True
    assert sol.isAnagram("a", "ab") is False

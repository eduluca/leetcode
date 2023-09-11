'''
217. Contains Duplicate
Easy
10.6K
1.2K
Companies
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        prevMap = {}

        for n in nums:
            if n in prevMap:
                return True
            prevMap[n] = True

        return False

nums = [1,2,3,1]
solution = Solution()
print(solution.containsDuplicate(nums))
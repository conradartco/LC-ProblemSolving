# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].


# List = [2,7,11,15]
# target = 9
# class Solution(object):
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         seen = {}
#         for i, value in enumerate(nums):
#             remaining = target - nums[i]

#             if remaining in seen:
#                 return [i, seen[remaining]]
            
#             seen[value] = i
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
        
nums = [2,7,11,15]
target = 9
class mySolution(object):
    def sumTwo(self, nums, target):
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - nums[i]

            if remaining in seen:
                return [i, seen[remaining]]

            seen[value] = i
# 1. Two Sum
# Solved
# Easy
# Hint
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for ind,val in enumerate(nums):
            complement = target - val
            if complement in seen:
                return[seen[complement],ind]
            seen[val]=ind
# This function finds the indices of two numbers in the list `nums` that add up to the given `target`.
#
# Steps:
# 1. Create a dictionary `seen` to store numbers we've already checked, with their indices as values.
# 2. Loop through the list using `enumerate` to get both index (`ind`) and value (`val`) at the same time.
# 3. For each number, calculate its complement (what value is needed to reach the target).
# 4. Check if this complement has already been seen:
#    - If yes, return the index of the complement and the current index as the solution.
#    - If not, store the current number and its index in the dictionary.
# 5. This approach ensures we find the solution in a single pass with O(n) time complexity.
'''
Accepted
63 / 63 testcases passed
priyanshvermaofficial
priyanshvermaofficial
submitted at Jul 16, 2025 21:13

Editorial

Solution
Runtime
0
ms
Beats
100.00%
Analyze Complexity
Memory
19.09
MB
Beats
23.65%
'''

"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:
Input: nums = [3,2,3]
Output: 3

Example 2:
Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""
from typing import List


class Solution:
    # Approach 1:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # def majorityElement(self, nums: List[int]) -> int:
    #     num_counts = {}
    #     max_nums = 0
    #     majority_element = None
    #     for num in nums:
    #         if num in num_counts:
    #             num_counts[num] += 1
    #         else:
    #             num_counts[num] = 1
    #
    #         if max_nums < num_counts[num]:
    #             max_nums = num_counts[num]
    #             majority_element = num
    #
    #     return majority_element

    # Approach 2:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # def majorityElement(self, nums: List[int]) -> int:
    #     num_counts = 0
    #     majority_element = nums[0]
    #     for num in nums:
    #         if num_counts == 0:
    #             majority_element = num
    #
    #         if num == majority_element:
    #             num_counts += 1
    #         else:
    #             num_counts -= 1
    #
    #     return majority_element

    # Approach 3:
    # Time Complexity: O(n log n)
    # Space Complexity: O(1)
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        majority_element = nums[len(nums) // 2]

        return majority_element


if __name__ == "__main__":
    nums = [3, 3, 4, 4, 4, 3, 3]
    solution = Solution()
    print(solution.majorityElement(nums))

"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        # Approach 1: slow due to .remove() operation which has O(n^2) time complexity
        # for num in nums:
        #     if num == 0:
        #         nums.remove(0)
        #         nums.append(0)

        # Approach 2: 2 pointer approach, it will have O(n) time complexity
        left_pointer = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[left_pointer], nums[i] = nums[i], nums[left_pointer]
                left_pointer += 1

        return nums


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    solution = Solution()
    print(solution.moveZeroes(nums))

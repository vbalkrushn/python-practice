"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.



Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]


Constraints:
1 <= nums.length <= 105
-231 <= nums[i] <= 231 - 1
0 <= k <= 105
"""
from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Approach 1:
        # Time Complexity: O(k)
        # Space Complexity: O(1)
        # for n in range(k):
        #     num = nums.pop(len(nums) - 1)
        #     print(num)
        #     nums.insert(0, num)

        # Approach 2: Optimal
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

        print(9 % 2)


if __name__ == "__main__":
    nums = [-1, -100, 3, 99]
    solution = Solution()
    solution.rotate(nums, 2)
    print(nums)

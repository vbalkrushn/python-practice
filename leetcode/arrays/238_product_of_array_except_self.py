"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.


Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.
"""
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Approach 1:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        nums_len = len(nums)
        result_product = [1] * nums_len

        # Calculate prefix product
        prefix_product = 1
        for i in range(nums_len):
            result_product[i] = prefix_product
            prefix_product *= nums[i]

        print(result_product)

        # Calculate suffix product
        suffix_product = 1
        for i in range(nums_len - 1, -1, -1):
            result_product[i] *= suffix_product
            suffix_product *= nums[i]

        return result_product


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    solution = Solution()
    print(solution.productExceptSelf(nums))

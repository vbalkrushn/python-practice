from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        if len(nums) > 1:
            max_length = 0
            element_sum = 0
            diff_index = {}
            for index, num in enumerate(nums):
                if num == 0:
                    element_sum -= 1
                else:
                    element_sum += 1

                if element_sum not in diff_index:
                    diff_index[element_sum] = index

                if element_sum == 0:
                    max_length = index + 1
                else:
                    idx = diff_index[element_sum]
                    max_length = max(max_length, index - idx)
            return max_length
        else:
            return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.findMaxLength([1, 1, 0, 0, 1, 1, 0, 1, 0, 1]))

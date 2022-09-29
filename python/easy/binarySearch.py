import math
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """ Perform a binary search on the sorted list nums to find the index of target.

        :param nums: sorted list
        :param target: target to find in nums
        :return: index of target
        """
        # start at middle
        current_index = math.floor(len(nums) / 2)
        # min and max limit for search
        min_limit, max_limit = 0, len(nums)

        # iterate search
        while nums[current_index] != target:
            # target larger than current -> search in right side of list, else on left
            if target > nums[current_index]:
                min_limit = current_index + 1
                current_index = math.floor(max_limit - (max_limit - min_limit) / 2)
            else:
                max_limit = current_index
                current_index = math.floor(min_limit + (max_limit - min_limit) / 2)

            # if nums contains no elements or current_index already visited return -1
            if max_limit - min_limit < 1:
                return -1

        return current_index


nums_input = [-1, 0, 3, 5, 9, 12]
target_input = 13

solution = Solution()
print(solution.search(nums_input, target_input))

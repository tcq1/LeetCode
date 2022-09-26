from typing import List


def pivotIndex(nums: List[int]) -> int:
    # empty list: return -1
    if not nums:
        return -1

    current_index = 0

    try:
        left_sum, right_sum = get_sum_left_right(nums, current_index)

        # check if equal
        while left_sum != right_sum:
            current_index += 1
            left_sum, right_sum = get_sum_left_right(nums, current_index)

        return current_index

    except IndexError:
        return -1


def get_sum_left_right(nums, pivot):
    if pivot not in range(len(nums)):
        raise IndexError
    return sum(nums[:pivot]), sum(nums[pivot + 1:])


input_list = [-1, -1, -1, -1, -1, 0]
pivotIndex(input_list)

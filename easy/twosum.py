from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    """ Idea: create a hash table with the numbers as index and list index as value.
        Iterate through each number of the list and check whether the complement that adds the number up to the target already exists in the hash table.
        If it exists look up the index, if not add the number and it's index to the hash table.
    """
    hashTable = {}
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashTable:
            return [hashTable[complement], i]
        hashTable[nums[i]] = i


print(twoSum([2, 7, 11, 15], 9))

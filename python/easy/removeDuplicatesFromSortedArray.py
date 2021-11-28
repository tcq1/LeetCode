class Solution:
    def removeDuplicates(self, nums):
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == nums[i-1]:
                del nums[i]

        return len(nums)


solution = Solution()
print(solution.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))

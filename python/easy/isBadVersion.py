import math


def isBadVersion(version: int) -> bool:
    return version in range(8, 20)


class Solution:
    def firstBadVersion(self, n: int) -> int:
        start, end = 0, n
        while start < end:
            mid = start + math.floor((end-start) / 2)
            # if mid is not bad version search in right half of list, else search in left
            if not isBadVersion(mid):
                start = mid + 1
            else:
                end = mid

        return start


solution = Solution()
print(solution.firstBadVersion(20))

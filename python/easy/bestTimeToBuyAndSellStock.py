from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """ Find the maximum profit by using two pointers: one pointer pointing at the buying point and one pointing at the selling point.
        Each time the buying point is smaller than the selling point update the buying pointer. That way the minimum can be found.

        :param prices: list of prices
        :return: maximum profit
        """
        max_profit = 0
        buy_pointer = 0
        sell_pointer = 1
        while sell_pointer < len(prices):
            current_profit = prices[sell_pointer] - prices[buy_pointer]
            if prices[sell_pointer] < prices[buy_pointer]:
                buy_pointer = sell_pointer
            else:
                max_profit = max(current_profit, max_profit)
            sell_pointer += 1

        return max_profit


price_list = [7, 1, 5, 3, 6, 4]
solution = Solution()
print(solution.maxProfit(price_list))

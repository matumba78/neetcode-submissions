class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        if len(prices) < 1:
            return res
        min_buy = prices[0]
        for n in range(1, len(prices)):
            profit = prices[n] - min_buy
            res = max(res, profit)
            if prices[n] < min_buy:
                min_buy = prices[n]
        return res

        
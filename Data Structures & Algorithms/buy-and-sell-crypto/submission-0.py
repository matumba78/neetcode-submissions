class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_so_far = prices[0]
        for num in range(1,len(prices)):
            if prices[num] < min_so_far:
                min_so_far = prices[num]
            else:
                profit = max(profit, prices[num] - min_so_far)
        return profit

            

        
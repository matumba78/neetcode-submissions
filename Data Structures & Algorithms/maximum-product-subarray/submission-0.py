class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #kadens algo
        res = float("-inf")
        currmax, currmin = 1, 1

        for num in nums:
            tmp = currmax * num
            currmax = max(tmp, num * currmin, num)
            currmin = min(tmp, num * currmin, num)
            res = max(currmax, res)
        return res
        
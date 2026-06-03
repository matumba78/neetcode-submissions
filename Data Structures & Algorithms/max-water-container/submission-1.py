class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0

        l, r = 0, len(heights) - 1

        while l < r:
            min_h = min(heights[l], heights[r])
            cap = min_h * (r - l)
            res = max(res, cap)
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res


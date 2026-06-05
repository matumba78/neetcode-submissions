class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        ans = 0
        max_left = height[left]
        max_right = height[right]
        while left < right:
            if max_left <= max_right:
                left += 1
                max_left = max(max_left, height[left])
                res = max_left - height[left]
                if res > 0:
                    ans += max_left - height[left]
            else:
                right -= 1
                max_right = max(max_right, height[right])
                res = max_right - height[right]
                if res > 0:
                    ans += max_right - height[right]
        return ans


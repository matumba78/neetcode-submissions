class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0]*(len(height))
        right_max = [0]*(len(height))
        for h in range(1,len(height) - 1):
            left_max[h] = max(left_max[h-1], height[h-1])
        for h in reversed(range(len(height)-1)):
            right_max[h] = max(height[h+1], right_max[h+1])
        res = 0
        for h in range(len(height) - 1):
            _min = min(left_max[h], right_max[h])
            if (_min - height[h]) > 0:
                res += (_min - height[h])
        return res



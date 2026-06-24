from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        bs = []
        bs.append(nums[0])
        for i in range(1, len(nums)):
            left, right = 0, len(bs)
            while left < right:
                mid = (left + right) // 2
                if bs[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid
            if bs[-1] < nums[i]:
                bs.append(nums[i])
            else:
                bs[left] = nums[i]
        return len(bs)

            
        
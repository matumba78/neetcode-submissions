from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        bs = []
        bs.append(nums[0])
        for i in range(1, len(nums)):
            if bs[-1] < nums[i]:
                bs.append(nums[i])
            else:
                idx = bisect_left(bs, nums[i])
                bs[idx] = nums[i]
        return len(bs)

            
        
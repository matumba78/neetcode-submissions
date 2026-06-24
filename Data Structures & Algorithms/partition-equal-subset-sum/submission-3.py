class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total//2
        
        summation = []
        summation.append(0)
        for i in range(len(nums) - 1, -1, -1):
            for j in range(len(summation)):
                tot = summation[j] + nums[i]
                if tot not in summation:
                    summation.append(tot)
                if target in summation:
                    return True
        return False


        
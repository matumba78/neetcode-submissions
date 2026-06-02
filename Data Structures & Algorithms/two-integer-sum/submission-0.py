class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i in range(len(nums)):
            b = target - nums[i]
            if b in seen.keys():
                return [seen[b], i]
            seen[nums[i]] = i

        
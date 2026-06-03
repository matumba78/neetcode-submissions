class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i in range(len(nums)):
            c = target - nums[i]
            if c in visited:
                return [visited[c], i]
            visited[nums[i]] = i
        
        
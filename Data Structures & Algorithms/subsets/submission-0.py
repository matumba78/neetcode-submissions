class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []

        curr_subset = []

        def dfs(i):
            if i > len(nums) - 1:
                subset.append(curr_subset.copy())
                return
            
            curr_subset.append(nums[i])
            dfs(i + 1)

            curr_subset.pop()
            dfs(i + 1)

        dfs(0)
        return subset
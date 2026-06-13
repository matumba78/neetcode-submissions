class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            if i > len(nums) - 1 or total > target:
                return
            
            curr.append(nums[i])
            #important we have send same num again and again so dont increment i
            #increment when not including this like in next iteration we have to get new no
            dfs(i, curr, total + nums[i])

            curr.pop()
            dfs(i + 1, curr, total)
        dfs(0, [], 0)
        return res
        
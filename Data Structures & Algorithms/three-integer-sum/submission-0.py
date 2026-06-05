class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        #two pointer approach
        # -4, -1, -1, 0, 1, 2
        res = []
        nums.sort()

        for i, num in enumerate(nums):
            if num > 0:
                break

            if i > 0 and nums[i] == nums[i-1]:
                continue

            ref = -num

            l, r = i + 1, len(nums) - 1

            while l < r:
                if nums[l] + nums[r] < ref:
                    l += 1
                elif nums[l] + nums[r] > ref:
                    r -= 1
                else:
                    res.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
                
        
        return res


        
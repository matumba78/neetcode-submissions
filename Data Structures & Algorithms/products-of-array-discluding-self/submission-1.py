class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_to_r = [1]*len(nums)
        r_to_l = [1]*len(nums)
        res = []
        prev = 1
        _next = 1
        for i in range(len(nums)):
            l_to_r[i] = nums[i] * prev
            prev = l_to_r[i]
        
        for i in reversed(range(len(nums))):
            r_to_l[i] = nums[i] * _next
            _next = r_to_l[i]
        for i in range(len(nums)):
            if i == 0:
                left = 1
            else:
                left = l_to_r[i-1]
            if i == len(nums) - 1:
                right = 1
            else:
                right = r_to_l[i+1]
            res.append(left * right)
        return res
            

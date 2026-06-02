class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        a1 = [1] * len(nums)
        a2 = [1] * len(nums)
        prev = 1
        for i in range(len(nums)):
            a1[i] = nums[i] * prev
            prev = a1[i]
        
        prev = 1
        for i in range(len(nums) - 1 , -1, -1):
            a2[i] = nums[i] * prev
            prev = a2[i]

        for i in range(len(nums)):
            left = a1[i - 1] if i > 0 else 1
            right = a2[i + 1] if i < len(nums) - 1 else 1
            res[i] = left * right
        return res


        
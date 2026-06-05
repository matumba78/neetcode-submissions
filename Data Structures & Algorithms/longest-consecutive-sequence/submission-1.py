class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_map = defaultdict(int)
        res = 0
        for num in nums:
            if not hash_map[num]:
                hash_map[num] = hash_map[num-1] + hash_map[num+1] + 1
                hash_map[num - hash_map[num - 1]] = hash_map[num]
                hash_map[num + hash_map[num + 1]] = hash_map[num]
            res = max(hash_map[num], res)
        return res

        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        count_to_freq = [[] for n in range(len(nums)+1)]
        res = []

        for n in nums:
            if n not in count:
                count[n] = 0
            count[n] += 1
        
        for n, v in count.items():
            count_to_freq[v].append(n)
        
        for i in count_to_freq[::-1]:
            for j in i:
                res.append(j)
                if len(res) == k:
                    return res

        
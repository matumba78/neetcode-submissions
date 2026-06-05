class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]
        for n in nums:
            if n not in count:
                count[n] = 0
            count[n] += 1
        for index, value in count.items():
            freq[value].append(index)
        res = []
        for i in reversed(range(len(nums)+1)):
            if freq[i]:
                for j in freq[i]:
                    res.append(j)
                    if len(res) == k:
                        return res        


        
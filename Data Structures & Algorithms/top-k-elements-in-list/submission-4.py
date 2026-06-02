class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        ans = []
        freq_arr = [[] for i in range(len(nums) + 1)]

        for n in nums:
            if n not in count:
                count[n] = 1
            else:
                count[n] += 1
        for n, coun in  count.items():
            freq_arr[coun].append(n)

        for i in range(len(freq_arr) - 1, -1, -1):
            for j in freq_arr[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans
        return []

        
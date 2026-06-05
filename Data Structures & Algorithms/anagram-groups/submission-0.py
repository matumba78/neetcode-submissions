class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for st in strs:
            freq = [0] * 26
            for s in st:
                freq[ord(s) - ord('a')] += 1
            if tuple(freq) not in res:
                res[tuple(freq)] = [st]
            else:
                res[tuple(freq)].append(st)
        return [value for _, value in res.items()]
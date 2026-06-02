class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for st in strs:
            freq_key = [0] * 26
            for c in st:
                freq_key[ord(c) - ord('a')] += 1
            if tuple(freq_key) in res:
                res[tuple(freq_key)].append(st)
            else:
                res[tuple(freq_key)] = [st]
        return list(res.values())

        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freq_s = {}
        for char in s:
            if char not in freq_s:
                freq_s[char] = 1
            else:
                freq_s[char] += 1
        for char in t:
            if char in freq_s.keys():
                freq_s[char] -= 1
                if freq_s[char] == 0:
                    del freq_s[char]
        if len(freq_s) == 0:
            return True
        return False
        
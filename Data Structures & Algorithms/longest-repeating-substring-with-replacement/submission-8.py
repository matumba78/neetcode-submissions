class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        res = 0
        l = 0
        max_freq = 0
        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            max_freq = max(max_freq, freq[s[r]])
            if r - l + 1 - max_freq > k:
                freq[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
        
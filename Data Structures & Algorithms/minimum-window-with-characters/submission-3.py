class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        window, counT = {}, {}

        for c in t:
            counT[c] = 1 + counT.get(c, 0)

        have, want = 0, len(counT)

        res, rlength = [-1, -1], float('inf')
        l = 0

        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            
            if s[r] in counT and window[s[r]] == counT[s[r]]:
                have += 1
            
            while have == want:
                if r - l + 1 < rlength:
                    rlength = r - l + 1
                    res = [l, r]
                window[s[l]] -= 1
                if s[l] in counT and window[s[l]] < counT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if rlength != float('inf') else ""

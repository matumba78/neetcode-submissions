class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for wrd in wordDict:
                if i + len(wrd) <= len(s) and s[i:i + len(wrd)] == wrd:
                    dp[i] = dp[i + len(wrd)]
                if dp[i]:
                    break
        return dp[0]
        
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1, text2 = text2, text1

        dp_curr = [0] * (len(text2) + 1)
        dp_prev = [0] * (len(text2) + 1)

        for i in range(len(text1) - 1, -1, -1):
            for j in range(len(text2) - 1, -1, -1):
                if text1[i] == text2[j]:
                    dp_curr[j] = 1 + dp_prev[j + 1]
                else:
                    dp_curr[j] = max(dp_prev[j], dp_curr[j + 1])
            dp_curr, dp_prev = dp_prev, dp_curr
        return dp_prev[0]
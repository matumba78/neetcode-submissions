class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        seen = [0]*26
        window = [0]*26

        l = 0

        for i in range(len(s1)):
            seen[ord(s1[i]) - ord('a')] += 1
            window[ord(s2[i]) - ord('a')] += 1
        if seen == window:
            return True
        
        for r in range(len(s1), len(s2)):
            
            window[ord(s2[r]) - ord('a')] += 1
            if r - l + 1 > len(s1):
                window[ord(s2[l]) - ord('a')] -= 1
                l += 1
            if seen == window:
                return True
        return False



        

        
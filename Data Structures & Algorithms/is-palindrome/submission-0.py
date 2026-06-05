class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if (ord(s[i]) < ord("A") or ord(s[i]) > ord("Z")) and (ord(s[i]) < ord("a") or ord(s[i]) > ord("z")) and (ord(s[i]) < ord("0") or ord(s[i]) > ord("9")):
                i += 1
                continue
            if (ord(s[j]) < ord("A") or ord(s[j]) > ord("Z")) and (ord(s[j]) < ord("a") or ord(s[j]) > ord("z")) and (ord(s[j]) < ord("0") or ord(s[j]) > ord("9")):
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -= 1
        return True
        
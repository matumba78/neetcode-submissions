class Solution:
    def isValid(self, s: str) -> bool:
        match_br = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []
        for c in s:
            if c in match_br:
                if stack and stack[-1] == match_br[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False


        
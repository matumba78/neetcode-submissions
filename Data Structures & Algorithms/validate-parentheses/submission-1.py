class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        for i in s:
            if stack and i == mp.get(stack[-1]):
                stack.pop()
            else:
                stack.append(i)
            print(stack)
        if len(stack) == 0:
            return True
        return False
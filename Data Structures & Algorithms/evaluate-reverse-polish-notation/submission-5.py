class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack =[]
        exp = ["+", "-", "/", "*"]
        ans = 0
        for n in tokens:
            if n in exp and len(stack) >=2:
                b = stack.pop()
                a = stack.pop()
                if n == "+":
                    ans = int(a) + int(b)
                elif n == "-":
                    ans = int(a) - int(b)
                elif n == "*":
                    ans = int(a) * int(b)
                elif n == "/":
                    ans = int(a) / int(b)
                stack.append(ans)
            else:
                stack.append(n)
        if stack:
            return int(stack[0])
        return ans
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            if t == "+":
                first_top = int(stack.pop())
                second_top = int(stack.pop())
                res = second_top + first_top
                stack.append(res)
            elif t =="-":
                first_top = int(stack.pop())
                second_top = int(stack.pop())
                res = second_top - first_top
                stack.append(res)
            elif t =="*":
                first_top = int(stack.pop())
                second_top = int(stack.pop())
                res = second_top * first_top
                stack.append(res)
            elif t == "/":
                first_top = int(stack.pop())
                second_top = float(stack.pop())
                res = float(second_top)/first_top
                stack.append(res)
            else:
                stack.append(t)
        print(stack)
        return int(stack[0])
        
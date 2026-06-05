class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []
        length = len(heights)
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                idx, ht = stack.pop()
                maxArea = max(maxArea, ht * (i - idx))
                start = idx
            stack.append([start, h])
        for i, h in stack:
            print(h, length, i)
            maxArea = max(maxArea, h * (length - i))
        return maxArea





        
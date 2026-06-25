class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i:i[0])

        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastval = output[-1][1]
            if start <= lastval:
                output[-1][1] = max(end, lastval)
            else:
                output.append([start, end])
        return output        
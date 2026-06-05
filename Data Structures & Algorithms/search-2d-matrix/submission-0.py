class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row, col = len(matrix), len(matrix[0])

        top, bot = 0, row - 1

        while top <= bot:
            mid = (top + bot) // 2
            if matrix[mid][-1] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                bot = mid - 1
            else:
                break
        print(top, bot)
        
        if top> bot:
            return False
        
        l, r = 0, col
        top = (top + bot )//2

        while l <= r:
            mid = (l + r) // 2
            if target < matrix[top][mid]:
                r = mid - 1
            elif target > matrix[top][mid]:
                l = mid + 1
            else:
                return True
        return False




        
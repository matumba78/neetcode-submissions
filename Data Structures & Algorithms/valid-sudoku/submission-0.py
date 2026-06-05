class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check rows
        for row in range(9):
            seen = set()
            for col in range(9):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in seen:
                    return False
                seen.add(board[row][col])
        #check cols
        for col in range(9):
            seen = set()
            for row in range(9):
                if board[row][col] == ".":
                    continue
                elif board[row][col] in seen:
                    return False
                seen.add(board[row][col])
        #check boxes
        for box in range(9):
            seen = set()
            for row in range(3):
                for col in range(3):
                    row_c = (box//3) * 3 + row
                    col_c = (box%3) * 3 + col
                    if board[row_c][col_c] == ".":
                        continue
                    elif board[row_c][col_c] in seen:
                        return False
                    seen.add(board[row_c][col_c])
        return True
                


        
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        print(rows, cols)
        visited = set()
        edge_cells = set()

        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visited or board[r][c] == "X":
                return
            
            visited.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for c in range(cols):
            if board[0][c] == "O":
                edge_cells.add((0, c))
        for c in range(cols):
            if board[rows - 1][c] == "O":
                edge_cells.add((rows - 1, c))
        
        for r in range(rows):
            if board[r][0] == "O":
                edge_cells.add((r, 0))
        for r in range(rows):
            print(r, cols - 1)
            if board[r][cols - 1] == "O":
                edge_cells.add((r, cols - 1))

        for r, c in edge_cells:
            dfs(r, c)
        print(visited)
        print(edge_cells)
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and (r, c) not in edge_cells:
                    board[r][c] = "X"
        

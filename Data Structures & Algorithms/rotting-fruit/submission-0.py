class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        fresh = 0
        time = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r,c])
        
        dire = [[1,0], [-1,0], [0, 1], [0,-1]]

        while q and fresh > 0:
            length = len(q)
            for i in range(length):
                r, c = q.popleft()
                for dr, dc in dire:
                    row, col = r + dr, c + dc
                    if row >= 0 and col >= 0 and row < rows and col < cols and grid[row][col] == 1:
                        grid[row][col] = 2
                        fresh -= 1
                        q.append([row, col])
            time += 1
        return time if fresh == 0 else -1

        
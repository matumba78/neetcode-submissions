class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])

        q = deque()
        visit = set()
        def add_cells(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == -1 or (r, c) in visit:
                return
            visit.add((r,c))
            q.append([r,c])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist if grid[r][c] else 0
                add_cells(r + 1, c)
                add_cells(r - 1, c)
                add_cells(r, c - 1)
                add_cells(r, c + 1)
            dist += 1

        
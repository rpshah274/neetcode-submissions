class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        area = 0
        directions = [(0,1),(1,0),(-1,0),(0,-1)]

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            grid[r][c] = 0
            count=1
            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if 0 <= row < m and 0 <= col < n and grid[row][col] == 1:
                        grid[row][col] = 0
                        count+=1
                        q.append((row, col))
            return count
                

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    area=max(area,bfs(i, j))
        return area
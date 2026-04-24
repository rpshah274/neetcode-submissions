class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n=len(grid)
        m=len(grid[0])
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        q=deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    q.append((i,j))
                  
        while q:
            l=len(q)
            for _ in range(l):
                r,c=q.popleft()
                for dr,dc in directions:
                    row=r+dr
                    col=c+dc
                    if (row in range(n) and col in range(m) and grid[row][col]==2147483647):
                        grid[row][col]=grid[r][c]+1
                        q.append((row, col))
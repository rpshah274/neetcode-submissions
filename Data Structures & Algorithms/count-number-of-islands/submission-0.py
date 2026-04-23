class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        count=0
        def bfs(r,c):
            q=deque()
            q.append((r,c))
            grid[r][c]=="0"
            while q:
                l=len(q)
                for i in range(l):
                    r,c=q.popleft()
                    for dr,dc in directions: 
                        row,col = r+dr,c+dc
                        if (row in range(m) and col in range(n) and grid[row][col]=="1"):
                            grid[row][col] = "0"
                            q.append((row, col))
        for i in range(m):
            for j in range(n):
                if grid[i][j] =="1":
                    count+=1
                    bfs(i,j)
        return count
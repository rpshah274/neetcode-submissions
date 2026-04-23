class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        fresh=0
        time=0
        q=deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    fresh+=1
                if grid[i][j]==2:
                    q.append((i,j))
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        def bfs():
            nonlocal fresh
            time = 0
            while fresh>0 and q:
                l=len(q)
                for i in range(l):
                    r,c=q.popleft()
                    for dr,dc in directions: 
                        row,col = r+dr,c+dc
                        if (row in range(m) and col in range(n) and grid[row][col]==1):
                            grid[row][col]=2
                            q.append((row,col))
                            fresh-=1
                time+=1
            return time
        time = bfs()
        return time if fresh == 0 else -1
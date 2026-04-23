class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n=len(board)
        m=len(board[0])
        visited=set()
        def solve(i,j,idx):
            if idx==len(word):
                return True
            if i < 0 or i >= n or j < 0 or j >= m:
                return False
            if (i,j) in visited:
                return False
            if board[i][j]!=word[idx]:
                return False
            visited.add((i,j))
            res= (solve(i+1,j,idx+1) or
            solve(i,j+1,idx+1) or
            solve(i-1,j,idx+1) or
            solve(i,j-1,idx+1))
            visited.remove((i,j))
            return res
        for i in range(n):
            for j in range(m):
                if board[i][j]==word[0]:
                    if solve(i,j,0):
                        return True
        return False
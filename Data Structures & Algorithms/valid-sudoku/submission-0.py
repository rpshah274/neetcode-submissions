class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_freq=[[False]*9 for _ in range(9)]
        col_freq=[[False]*9 for _ in range(9)]
        Box=[[False]*9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                BI=(i//3)*3+(j//3)
                if board[i][j]!='.':
                    num=ord(board[i][j])-ord('1')
                    if row_freq[i][num] or col_freq[num][j] or Box[BI][num]:
                        return False
                    row_freq[i][num] = col_freq[num][j] = Box[BI][num] = True
        return True

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        w=[]
        for s in strs:
            w.append((s.count('0'),s.count('1')))
        dp = [[0]*(n+1) for _ in range(m+1)]
        for z,o in w:
            for i in range(m,z-1,-1):
                for j in range(n,o-1,-1):
                    dp[i][j]=max(dp[i][j],1+dp[i-z][j-o])
        return dp[m][n]

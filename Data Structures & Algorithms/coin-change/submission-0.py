class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF=float('inf')
        dp=[[INF]*(amount+1) for _ in range(len(coins)+1)]
        for i in range(1,len(coins)+1):
            dp[i][0]=0
        for i in range(amount+1):
            if i%coins[0]==0:
                dp[1][i]=i//coins[0]
        for i in range(2,len(coins)+1):
            for j in range(1,amount+1):
                if coins[i-1]<=j:
                    dp[i][j]=min(dp[i-1][j],1+dp[i][j-coins[i-1]])
                else:
                    dp[i][j]=dp[i-1][j]
        return -1 if dp[len(coins)][amount] == INF else dp[len(coins)][amount]
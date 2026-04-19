class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # p2=cost[0]
        # p1=cost[1]
        # for n in range(2,len(cost)):
        #     temp=cost[n]+min(p1,p2)
        #     p2=p1
        #     p1=temp
        # return min(p1,p2)
        dp={}
        def solve(n):
            if n>=len(cost):
                return 0
            if n in dp:
                return dp[n]
            dp[n]=cost[n]+min(solve(n+1),solve(n+2))
            return dp[n]
        return min(solve(0),solve(1))
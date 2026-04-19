class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        p2=cost[0]
        p1=cost[1]
        for n in range(2,len(cost)):
            temp=cost[n]+min(p1,p2)
            p2=p1
            p1=temp
        return min(p1,p2)
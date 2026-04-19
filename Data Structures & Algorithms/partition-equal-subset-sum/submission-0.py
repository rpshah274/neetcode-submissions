class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total=0
        for n in nums:
            total+=n
        if total%2!=0:
            return False
        sub_sum=total//2
        dp=[False]*(sub_sum+1)
        dp[0]=True
        for n in nums:
            for i in range(sub_sum,n-1,-1):
                dp[i]=dp[i] or dp[i-n]
        return dp[sub_sum]
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total=0
        for n in nums:
            total+=n
        if (total+target)%2!=0 or abs(target) > total:
            return 0
        sub_sum=(total+target)//2
        n=len(nums)
        dp=[0]*(sub_sum+1)
        dp[0]=1
        for n in nums:
            for i in range(sub_sum,n-1,-1):
                dp[i]+=dp[i-n]
        return dp[sub_sum]

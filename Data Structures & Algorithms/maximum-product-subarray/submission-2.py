class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mini=maxi=1
        res=nums[0]
        for n in nums:
            if n==0:
                mini=maxi=1
            temp=n*maxi
            maxi=max(n,mini*n,maxi*n)
            mini=min(n,mini*n,temp)
            res=max(res,maxi)
        return res

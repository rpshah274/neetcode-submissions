class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        sol=[]
        n=len(nums)
        def backtract(start,remain):
            if remain==0:
                res.append(sol[:])
                return
            if start>=n:
                return
            #Taken
            if nums[start]<=remain:
                sol.append(nums[start])
                backtract(start,remain-nums[start])
                sol.pop()
            #Not Taken
            backtract(start+1,remain)
        backtract(0,target)
        return res
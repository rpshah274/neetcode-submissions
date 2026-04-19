class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(arr):
            p1,p2=0,0
            for n in arr:
                taken=n+p1
                not_taken=p2
                p1=p2
                p2=max(taken,not_taken)
            return p2
        if len(nums)==1:
            return nums[0]
        return max(solve(nums[:-1]),solve(nums[1:]))

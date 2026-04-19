class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        start=0
        end=n-1
        if target < nums[0]:
            return -1
        while start<=end:
            mid= start + (end-1//2)
            if target>nums[mid]:
                start=mid+1
            elif target<nums[mid]:
                end=mid-1
            else:
                return mid
        return -1



        
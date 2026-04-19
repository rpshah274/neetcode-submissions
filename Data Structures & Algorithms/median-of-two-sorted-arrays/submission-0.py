class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B=nums1,nums2
        total=len(A)+len(B)
        half=total//2
        if len(B)<len(A):
            A,B=B,A
        l,r=0,len(A)-1
        while True:
            i=(l+r)//2
            j=half-i-2
            aleft=A[i] if i>=0 else float('-inf')
            aright=A[i+1] if i+1<len(A) else float('inf')
            bleft=B[j] if j>=0 else float('-inf')
            bright=B[j+1] if j+1<len(B) else float('inf')
            if aright>=bleft and bright>=aleft:
                if total%2:
                    return min(aright,bright)
                else:
                    return (max(aleft,bleft)+min(aright,bright))/2
            elif aright<bleft:
                l=i+1
            else:
                r=i-1

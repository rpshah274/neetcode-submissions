class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n=len(s)
        end_index={}
        for i in range(n):
            end_index[s[i]]=i
        res=[]
        start=0
        end=0
        for k in range(n):
            end=max(end,end_index[s[k]])
            if k==end:
                res.append(end-start+1)
                start=end+1
        return res

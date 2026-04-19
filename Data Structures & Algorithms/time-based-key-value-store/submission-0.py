class TimeMap:

    def __init__(self):
      self.TimeMap={}  

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.TimeMap:
            self.TimeMap[key]=[]
        self.TimeMap[key].append((timestamp,value))   

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.TimeMap:
            return ""
        arr=self.TimeMap[key]
        res=""
        l,r=0,len(arr)-1
        while l<=r:
            mid=(l+r)//2
            if arr[mid][0]<=timestamp:
                res=arr[mid][1]
                l=mid+1
            else:
                r=mid-1
        return res
class MedianFinder:
    def __init__(self):
        self.heap_min=[]
        self.heap_max=[]

    def addNum(self, num: int) -> None:
        if self.heap_max and num > self.heap_max[0]:   
            heapq.heappush(self.heap_max,num)
        else:
            heapq.heappush(self.heap_min,-1*num)
        if len(self.heap_max)>len(self.heap_min)+1: 
            v=heapq.heappop(self.heap_max)
            heapq.heappush(self.heap_min,-1*v)
        if len(self.heap_min)>len(self.heap_max)+1: 
            v=heapq.heappop(self.heap_min)
            heapq.heappush(self.heap_max,-1*v)
    def findMedian(self) -> float:
        if len(self.heap_max)<len(self.heap_min):
            return -1*self.heap_min[0]
        if len(self.heap_max)>len(self.heap_min):
            return self.heap_max[0]
        return  (self.heap_max[0] + (-1*self.heap_min[0]))/2
        
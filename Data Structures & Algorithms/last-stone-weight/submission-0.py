class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)
        def solve():
            if not heap:
                return 0

            if len(heap) == 1:
                return -heap[0] 

            x=-heapq.heappop(heap)
            y=-heapq.heappop(heap)

            if x!=y:
                heapq.heappush(heap,-(x-y))
            return solve()
        return solve()

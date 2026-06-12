class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        maxHeap = [-n for n in stones]
        heapq.heapify(maxHeap)
        print(maxHeap)
        while len(maxHeap) > 1:
            val1 = -heapq.heappop(maxHeap)
            val2 = -heapq.heappop(maxHeap)
            print(val1-val2)
            if (val1 - val2) != 0:
                heapq.heappush(maxHeap, -(val1 - val2))
        print(maxHeap)
        if not maxHeap:
            return 0
        else:
            return -maxHeap[0]

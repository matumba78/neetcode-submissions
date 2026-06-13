class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-c for c in count.values()]
        heapq.heapify(max_heap)

        q = deque()
        time = 0

        while max_heap or q:
            time += 1
            if max_heap:
                data = heapq.heappop(max_heap)
                data += 1
                if data:
                    q.append([data, time + n])
            if q and q[0][1] == time:
                data2 = q.popleft() 
                heapq.heappush(max_heap, data2[0])
        return time



        
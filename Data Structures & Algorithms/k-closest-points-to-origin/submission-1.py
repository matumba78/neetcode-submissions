class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        hash_map = {}
        for i in range(len(points)):
            res = -math.sqrt(points[i][0]*points[i][0] + points[i][1]*points[i][1])

            distance.append(res)
            if not hash_map.get((res), None):
                hash_map[(res)] = [points[i]]
            else:
                hash_map[(res)].append(points[i])
        heapq.heapify(distance)
        while len(distance) > k:
            heapq.heappop(distance)
        r = []
        for i in range(len(distance)):
            if distance[i] in hash_map:
                r += hash_map[distance[i]]
                del hash_map[distance[i]]
        return r

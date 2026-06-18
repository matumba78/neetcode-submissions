class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dep_count = [0] * numCourses
        neighbours = [[] for _ in range(numCourses)]
        for i in range(len(prerequisites)):
            dep_count[prerequisites[i][1]] += 1
            neighbours[prerequisites[i][0]].append(prerequisites[i][1])
        
        q = deque()

        for d in range(len(dep_count)):
            if dep_count[d] == 0:
                q.append(d)
        
        count, res = 0, []

        while q:
            node = q.popleft()
            count += 1
            res.append(node)
            for nei in neighbours[node]:
                dep_count[nei] -= 1
                if dep_count[nei] == 0:
                    q.append(nei)
        if count != numCourses:
            return []
        return res[::-1]

        
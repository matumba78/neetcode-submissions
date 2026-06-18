class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dep_count = [0] * numCourses
        neighbours = [[] for _ in range(numCourses)]
        for i in range(len(prerequisites)):
            dep_count[prerequisites[i][1]] += 1
            neighbours[prerequisites[i][0]].append(prerequisites[i][1])
        
        q = deque()
        for n in range(numCourses):
            if dep_count[n] == 0:
                q.append(n)

        count = 0
        while q:
            node = q.popleft()
            count += 1
            for nei in neighbours[node]:
                dep_count[nei] -= 1
                if dep_count[nei] == 0:
                    q.append(nei)
        return count == numCourses
                



        
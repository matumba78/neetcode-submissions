class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = [[] for _ in range(n)]

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        
        visit = set()

        def bfs(nod):
            q = deque([nod])
            visit.add(nod)
            while q:
                print(q)                
                node = q.popleft()
                for nei in adj_list[node]:
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei) 


        ans = 0
        for i in range(n):
            if i not in visit:
                bfs(i)
                ans += 1
                prev = i
        return ans


        
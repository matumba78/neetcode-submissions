class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(n)]

        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        q = deque()
        q.append([0, -1]) 
        # and node and parent so that we can skil if coming from parent as this is un directed graph
        visit = set()
        while q:
            node, parent = q.popleft()
            visit.add(node)
            for nei in adj_list[node]:
                if nei == parent:
                    continue
                if nei not in visit:
                    visit.add(nei)
                    q.append([nei, node])
                else:
                    return False
        return len(visit) == n


        
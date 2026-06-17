"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        oldnew = {}
        oldnew[node] = Node(node.val)
        q = deque([node])
        while q:
            curr = q.popleft()
            for nd in curr.neighbors:
                if nd not in oldnew:
                    cp = Node(nd.val)
                    oldnew[nd] = cp
                    q.append(nd)
                oldnew[curr].neighbors.append(oldnew[nd])
        return oldnew[node]
        
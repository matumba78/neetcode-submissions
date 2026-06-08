# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        max_so_far = root.val
        self.res = 0
        def dfs(root, max_so_far):
            if not root:
                return None
            if root.val >= max_so_far:
                self.res += 1
            max_so_far = max(max_so_far, root.val)
            return dfs(root.left, max_so_far) or dfs(root.right, max_so_far)
            
        dfs(root, root.val)
        return self.res
        
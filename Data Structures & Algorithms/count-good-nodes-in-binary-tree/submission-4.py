# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        def dfs(curr, max_so_far):
            if not curr:
                return 0
            if curr.val >= max_so_far: 
                res = 1
            else:
                res = 0
            max_so_far = max(max_so_far, curr.val)
            res += dfs(curr.left, max_so_far)
            res += dfs(curr.right, max_so_far)
            return res
        return dfs(root, root.val)
        
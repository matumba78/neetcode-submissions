# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = 0
        def dfs(root, k):
            if not root:
                return 0
            left = dfs(root.left, k)
            self.res += 1
            if self.res == k:
                return root.val
            right = dfs(root.right, k)
            return left or right
        return dfs(root, k)
        
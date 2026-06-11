# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
 
    
    # Encodes a tree to a single string.
class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.ino = []
        self.pre = []
        root1, root2 = root, root
        def inorder(root):
            if not root:
                return None
            inorder(root.left)
            self.ino.append(str(root.val) + ",")
            inorder(root.right)
    
        def preorder(root):
            if not root:
                return
            self.pre.append(str(root.val) + ",")
            preorder(root.left)
            preorder(root.right)
        inorder(root1)
        preorder(root2)
        res = "".join(self.pre) + "#" + "".join(self.ino)
        return res

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if len(data) == 1:
            return None
        t = data.split("#")
        print(t)
        print(t[0].split(",")[:-1], t[1].split(",")[:-1])
        def dfs(preorder, inorder):
            if not preorder or not inorder:
                return None
            root = TreeNode(preorder[0])
            for i,v in enumerate(inorder):
                if v == preorder[0]:
                    mid = i

            root.left = dfs(preorder[1: mid + 1], inorder[:mid])
            root.right = dfs(preorder[mid+1:], inorder[mid + 1:])
            return root
        print(list(t[0]), list(t[1]))
        return dfs(t[0].split(",")[:-1], t[1].split(",")[:-1])
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def __init__(self):
        self.arr = []
    def inorderTraversal(self, root):
        if not root:
            return []
        if root.left:
            self.inorderTraversal(root.left)
        self.arr.append(root.val)
        if root.right:
            self.inorderTraversal(root.right)
        return self.arr
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        q = [root]
        arr = []
        while len(q) > 0:
            size = len(q)
            arr.append([i.val for i in q if i])
            for _ in range(size):
                node = q.pop(0)
                if not node:
                    break
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return arr
        ind = 0
        
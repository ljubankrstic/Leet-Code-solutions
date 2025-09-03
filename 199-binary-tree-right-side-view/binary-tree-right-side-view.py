# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []
        q = [root]
        lastels = []
        while q:
            ln = len(q)
            for i in range(ln -1, -1, -1):
                if q[i]:
                    lastels.append(q[i].val)
                    break
            for i in range(ln):
                curr = q.pop(0)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        return lastels 

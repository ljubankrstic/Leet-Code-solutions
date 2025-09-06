# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        if not root:
            return []
        q = [root]
        levels = []
        while len(q):
            ln = len(q)
            level = []
            for _ in range(ln):
                curr = q.pop(0)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                level.append(curr.val)
            levels.append(level)
        return levels[::-1]

        
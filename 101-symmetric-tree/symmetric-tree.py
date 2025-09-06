# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        q = [root]
        while len(q):
            ln = len(q)
            level = []
            for i in range(ln):
                curr = q.pop(0)
                if curr:
                    q.append(curr.left)
                    q.append(curr.right)
                    level.append(curr.val)
                else:
                    level.append(None)
            for i in range(len(level) / 2):
                if level[i] != level[len(level) - 1 - i]:
                    return False
        return True
                
        
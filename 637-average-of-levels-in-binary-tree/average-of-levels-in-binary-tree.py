# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        q = [root]
        resarr = []
        while len(q) > 0:
            ln = len(q)
            curr_lvl = []
            for _ in range(ln):
                curr = q.pop(0)
                if curr:
                    curr_lvl.append(curr.val)
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
            resarr.append(sum(curr_lvl) / float(len(curr_lvl)))
        return resarr
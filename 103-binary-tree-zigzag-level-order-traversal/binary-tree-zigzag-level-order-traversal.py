# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        direction = 1
        if root == None:
            return []
        q = [root]
        levels = []
        while len(q):
            size = len(q)
            level = []
            for i in range(size):
                curr = q.pop(0)
                level.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            if direction == 1:
                levels.append(level)
            elif direction == -1:
                levels.append(level[::-1])
            direction *= -1
        return levels
        
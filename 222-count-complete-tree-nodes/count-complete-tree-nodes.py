
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def countNodes(self, root):
        if root is None:
            return 0
        nodes = [root]
        count = 0
        curr = None
        while len(nodes) > 0:
            curr = nodes.pop()
            if curr.left:
                nodes.append(curr.left)
            if curr.right:
                nodes.append(curr.right)
            count += 1
        return count
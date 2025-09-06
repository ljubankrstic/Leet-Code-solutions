"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        q = [root]
        levels = []
        while len(q) > 0:
            ln = len(q)
            level = []
            for _ in range(ln):
                curr = q.pop(0)
                for i in curr.children:
                    if i:
                        q.append(i)
                level.append(curr.val)
            levels.append(level)
        return levels

        
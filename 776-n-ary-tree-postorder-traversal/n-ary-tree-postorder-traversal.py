"""
# Definition for a Node.
class Node(object):
	def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution(object):
    def __init__(self):
        self.arr = []
    def postorder(self, root):
        if not root:
            return
        for i in root.children:
            self.postorder(i)
        self.arr.append(root.val)
        return self.arr
        
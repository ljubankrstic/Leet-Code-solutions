# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def addvalue2list(arr, node):
    if node.left:
        addvalue2list(arr, node.left)
    arr.append(node.val)
    if node.right:
        addvalue2list(arr, node.right)
class Solution(object):
    def getMinimumDifference(self, root):
        arr = []
        addvalue2list(arr, root)
        mindif = float('Inf')
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] < mindif:
                mindif = arr[i] - arr[i - 1]
        return mindif
        
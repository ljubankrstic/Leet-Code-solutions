# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        st = []
        while head:
            st.append(head.val)
            head = head.next
        return st == st[::-1]
        
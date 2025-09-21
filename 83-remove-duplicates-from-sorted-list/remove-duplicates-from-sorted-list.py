# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        curr = head
        while curr:
            if not curr.next:
                break
            while curr.next:
                if curr.next.val != curr.val:
                    break
                temp = curr.next.next
                curr.next.next = None
                curr.next = temp
            curr = curr.next
        return head
        
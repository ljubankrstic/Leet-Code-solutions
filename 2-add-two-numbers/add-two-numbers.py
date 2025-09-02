# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = ListNode((l1.val + l2.val) % 10)
        carry = (l1.val + l2.val) // 10
        curr = head
        l1 = l1.next
        l2 = l2.next
        while l1 and l2:
            curr.next = ListNode((l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) // 10
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            curr.next = ListNode((l1.val + carry) % 10)
            carry = (l1.val + carry) // 10
            curr = curr.next
            l1 = l1.next
        while l2:
            curr.next = ListNode((l2.val + carry) % 10)
            carry = (l2.val + carry) // 10
            curr = curr.next
            l2 = l2.next
        if carry > 0:
            curr.next = ListNode(carry)
        return head
        
        
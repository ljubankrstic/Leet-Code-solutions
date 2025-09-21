# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1
        head = ListNode()
        if list1.val > list2.val:
            head.val = list2.val
            list2 = list2.next
        else:
            head.val = list1.val
            list1 = list1.next
        curr = head
        print("hello")
        while list1 and list2:
            temp = ListNode()
            if list1.val > list2.val:
                temp.val = list2.val
                list2 = list2.next
            else:
                temp.val = list1.val
                list1 = list1.next
            curr.next = temp
            curr = curr.next
        print("hi")
        while list1:
            temp = ListNode()
            temp.val = list1.val
            list1 = list1.next
            curr.next = temp
            curr = curr.next
        print("ho")
        while list2:
            temp = ListNode()
            temp.val = list2.val
            list2 = list2.next
            curr.next = temp
            curr = curr.next
        return head

        
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        root = n = ListNode(0)
        while 1:
            if l1 == None:
                n.next = l2
                break
            elif l2 == None:
                n.next = l1
                break
            if l2.val <= l1.val:
                val = l2.val
                l2 = l2.next
            else:
                val = l1.val
                l1 = l1.next
            n.next = ListNode(val)
            n = n.next
        return root.next

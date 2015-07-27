# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        if l1 == None: return l2
        if l2 == None: return l1

        if l1.val > l2.val:
            p = l2
            q = l1
        else:
            p = l1
            q = l2

        h = p


        while p != None and q != None:
            if p.val <= q.val:
                #print "X"
                x = p
                p = p.next
            else:
                #print "Y"
                x.next = q
                
                q = p
                p = x.next
                x = p.next
                
        l = h
        while l.next != None:
            l = l.next

        if p != None:
            l.next = p
        else:
            l.next = q

        return h

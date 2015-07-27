# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):

        while head and head.val == val:
            head = head.next

        if head == None: return head

        p = head
        q = head.next

        while q:
            while q and q.val == val:
                q = q.next
            #print "p", p.val, "q", q.val,
            p.next = q
            p = q

            if q:
                q = q.next
        

        return head        
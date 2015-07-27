# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        if head == None: return None
        if n == 0: return head
        #if n == 1 and head.next == None: return None

        l = 0 
        x = head
        while x:
            l += 1
            x = x.next
        print l
        if n == l:
            return head.next

        p = head
        q = head
        
        for i in xrange(n):
            p = p.next

        while p.next != None:
            p = p.next            
            q = q.next

        q.next = q.next.next

        return head
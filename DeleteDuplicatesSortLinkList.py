# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if head == None:
            return head
        if head.next == None:
            return head
        p = head 
        while p != None:
            q = p.next
            while q != None:
                if p.val == q.val:
                    q = q.next
                else:
                    break
            p.next = q
            p = q

        return head        
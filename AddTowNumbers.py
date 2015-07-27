# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        cur = ListNode(0)
        ret = cur
        sum = 0
        
        while True:
            if l1 == None or l2 == None:
                break
                
            cur.next = ListNode(0)
            cur = cur.next
            
            sum = l2.val + l1.val
            
            l1 = l1.next
            l2 = l2.next
            if l1 
                
        return ret

        
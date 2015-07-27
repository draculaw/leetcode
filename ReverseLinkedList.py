# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def myRevertList(l):
    if l == None:
        return None
    if l.next == None:
        return l

    h = l
    l2 = None

    
    while h:
        t = h      
        h = h.next
        t.next = l2
        l2 = t

    return l2        
    
class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        return myRevertList(head)
        
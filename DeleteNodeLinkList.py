# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} node
    # @return {void} Do not return anything, modify node in-place instead.
    def deleteNode(self, node):

        if node == None or node.next == None: return 

        r = node
        p = node
        q = node.next
        while q:
            p.val = q.val 
            r = p
            p = q
            q = q.next
        
        r.next = None
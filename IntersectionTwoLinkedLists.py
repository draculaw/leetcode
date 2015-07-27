# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA == None or headB == None:
            return None

        la = 0
        lb = 0
        p = headA
        while p.next != None:
            p = p.next
            la += 1
        q = headB
        while q.next != None:
            q = q.next 
            lb += 1
            
        if q != p: return None
        
        n = la - lb
        p = headA
        q = headB
        if n > 0:
            while n > 0:
                p = p.next
                n -= 1
        else:
            n = -n
            while n > 0:
                q = q.next
                n -= 1
        
        while p != q:
            p = p.next
            q = q.next

        if p != None:
            print "p", p.val                    

        if q != None:
            print "q", q.val                    
        return p       
            
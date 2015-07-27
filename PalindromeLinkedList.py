# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        if head == None: return True
        if head.next == None: return True
        
        n = 0
        p = head
        while p:
            p = p.next
            n += 1
        n = n / 2
                
        p = head

        while n:
            q = p
            p = p.next
            n = n - 1

        q.next = None
        l = head 
        
        m = myRevertList(p)

        while l:
            
            if l.val != m.val:
            
                return False
            l = l.next
            m = m.next


        if m != None and m.next != None :
            
            return False

        return True

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
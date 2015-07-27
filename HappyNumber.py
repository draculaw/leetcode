class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        
        li = set()
        
        while True:
            
            if n == 1: return True
            s = str(n)
            n = sum([int(i)**2 for i in s])
            if n in li: return False
            li.add(n)           
            
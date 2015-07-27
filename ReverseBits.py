class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        
        s = bin(n)[2:]
        l = len(s)
        s = "0"*(32-l) + s
        
        s = s[::-1]
        
        s = int(s, 2)
        return s
class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        
        if n == 0: return 0
        i = 1
        while n & (n - 1):
            i += 1
            n = n & (n - 1)
        return i

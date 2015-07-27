class Solution:
    # @param {integer} n
    # @return {boolean}
    def isPowerOfTwo(self, n):
        if n == 0: return False
        return (not n < 0) and (n & (n - 1) == 0)
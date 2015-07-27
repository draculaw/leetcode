class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        
        r = 0
        while n:
            r += n/5
            n /= 5

        return r
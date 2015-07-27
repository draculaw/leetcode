class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        m = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        n = 0
        for c in s:
            n = n * 26 + m.index(c) + 1

        return n
        
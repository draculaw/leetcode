class Solution:
    # @param {integer} n
    # @return {string}
    def convertToTitle(self, n):
        m = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        s = ""
        while n:
            c = m[(n - 1) % 26]
            if c == "Z": n = n - 26
            n = n / 26
            s = c + s
        return s
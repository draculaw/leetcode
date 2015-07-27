class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        
        m = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        s = s.upper()
        s = [c for c in s if c in m]
        l = len(s)
        h = l / 2
        
        s2 = s[h:][::-1]
        for i in xrange(h):
            if s[i] != s2[i]:
                return False

        return True
        
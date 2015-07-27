

class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):


        if len(p) == 0 or len(s) == 0:
            return len(s) == len(p)

        if len(p) == 1:
            if len(s) == 1:
                return p[0] == '.' or p[0] == s[0]
            else:
                return False
                
        if p[1] == '*':
            while len(s) > 0 and (p[0] == '.' or s[0] == p[0]):
                if self.isMatch(s, p[2:]): 
                    return True
                s = s[1:]
            return self.isMatch(s, p[2:])
        elif (len(s) > 0 and p[0] == '.') or s[0] == p[0]:
            return self.isMatch(s[1:], p[1:])

        return False
        
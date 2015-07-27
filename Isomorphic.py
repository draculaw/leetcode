class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        l = len(s)
        if l < 2: return True

        return myIsomorphic(s,t,l) and myIsomorphic(t,s,l)          
      

def myIsomorphic(s,t,l):        

    m = {}
    for i in xrange(l):
        if not s[i] in m:
            m[s[i]] = t[i]
        else:
            if m[s[i]] != t[i]:
                return False

    return True        
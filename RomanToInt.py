RomanIntMap = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        
        s = s.replace(' ', '')
        s = s[::-1]
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return RomanIntMap[s]

        result = RomanIntMap[s[0]]
        
        for i in xrange(1, len(s) ):

            n = RomanIntMap[s[i]]
            if n < result and n < RomanIntMap[s[i-1]]:
                result = result - n
            else:
                result = n + result

        
        return result

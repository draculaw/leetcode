class Solution:
    # @param {string[]} strs
    # @return {string}
    def longestCommonPrefix(self, strs):

        ls = len(strs)
        if ls == 0: return ""
        if ls == 1: return strs[0]
        lengths = [len(s) for s in strs]
        length = min(lengths)
        result = ""
        for i in xrange(length) :
            
            c = strs[0][i]
            result += c
            for j in xrange(1,ls):
                if strs[j][i] != c:
                    result = result[:-1]
                    return result
            
        return result
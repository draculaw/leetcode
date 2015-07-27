class Solution:
    # @param {string} version1
    # @param {string} version2
    # @return {integer}
    def compareVersion(self, version1, version2):

        v1 = version1.split('.')
        v2 = version2.split('.')
        
        l1 = len(v1)
        l2 = len(v2)
        r = 1
        if l1 < l2:
            t = v2
            v2 = v1 
            v1 = t

            t = l2
            l2 = l1 
            l1 =  t
            r = -1


        for i in xrange(l2):
            if int(v1[i]) > int(v2[i]): return 1 * r
            elif int(v1[i]) < int(v2[i]): return -1 * r
        
        if l1 != l2:
            for i in xrange(l2, l1):
                if int(v1[i]) != 0: return 1 * r

        return 0
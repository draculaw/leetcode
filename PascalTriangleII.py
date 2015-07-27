class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        a = [1]
        for i in xrange(rowIndex):
            a = [sum(j) for j in zip([0] + a, a + [0])]

        return a
        
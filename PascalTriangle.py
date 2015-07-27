class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        
        g = pas_triangles()
        r = []
        for n in range(numRows):
            r.append(next(g))

        return r

def pas_triangles():
    a = [1]
    while True:
        yield a
        a = [sum(i) for i in zip([0] + a, a + [0])]
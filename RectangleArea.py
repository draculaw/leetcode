class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        
        result = (D - B) * (C - A) + (H - F) * (G - E)
        A1 = max(A, E)
        B1 = max(B, F)
        C1 = min(C, G)
        D1 = min(D, H)
        if B1 >= D1 or A1 >= C1:return result
        return result - (D1 - B1) * (C1 - A1)
class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        if x == 0:
            return 0

        pid = 0
        if x < 0:
            pid = 1
            x = -x
        s = str(x)
        s = s[::-1]
        
        x = int(s)
        if x >= (1 << 31): x = 0
        if pid:
            x = -x
        return x        

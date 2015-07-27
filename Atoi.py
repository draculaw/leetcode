class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        r = 0
        sig = 0


        for c in str:
            
            if sig == 0:
                if c == "+":
                    sig = 10
                elif c == '-':
                    sig = 11
                elif c <= '9' and c >= '0':
                    sig = 10 
                    r = int(c)
                elif c == ' ':
                    pass
                else:
                    return 0
            else:
                if c > '9' or c < '0':
                    break
                r = 10 * r + int(c)
            
        if sig == 11:
            r = -r
            
        if r > 2147483647:
            r = 2147483647
        
        if r < -2147483648:
            r = -2147483648
        return r


        
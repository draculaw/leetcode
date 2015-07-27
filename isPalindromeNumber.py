class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        
        if x < 0:
            return False

        if x < 10:
            return True

        i = 0
        y = x
        j = 0

        while y > 9:
            y = y / 10
            j += 1
        
        
        while i < j:
            a = pow(10, j)
            b = pow(10, i)
        
            a = (x/a) % 10
            b = (x/b) % 10

            i += 1
            j -= 1
           

            if a != b:
                print a, b, x, i, j
                return False
        
        return True

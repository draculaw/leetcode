
    
class Solution:
    # @param {string} s
    # @return {string}
    def longestPalindrome(self, s):
        
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s
        s2 = s
        s2 = "#*" + "*".join(s2) + "*"
        count = [0] * len(s2)

        index = 0
        max_len = 0

        for i in range(1, len(s2)):
            if max_len > i:
                count[i] = min (count[2*index - i], count[index] + index - i)
            else:
                count[i] = 1
            while i-count[i] >=0 and i+count[i] < len(s2) and s2[i-count[i]]==s2[i+count[i]]:
                count[i] += 1                
            
            if max_len < count[i]+i:
                max_len = count[i] + i
                index = i
            i+=1
        
        m = max(count)
        indexr = count.index(m)
        
        r =  s2[indexr-m : indexr+m]
        r1 = [r[i] for i in range (1, len(r)) if i%2 == 0 ]
        return ("").join(r1)

        
class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstring(self, s):

        max_sub = ''
        cur_sub = ''
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        
        i = -1
        for c in s:
            try:
                i = cur_sub.index(c)
            except:
                cur_sub += c
            else:
                if len(cur_sub) > len(max_sub):
                    max_sub = cur_sub   
                cur_sub = cur_sub[i+1:] + c
        
        if len(cur_sub) > len(max_sub):
            max_sub = cur_sub   

        
        return len(max_sub)
        
        
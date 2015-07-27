class Solution:
    # @param {string} digits
    # @return {string[]}
    def letterCombinations(self, digits):
        if len(digits) == 0: return []
        if len(digits) == 1: return keymap[digits]
                
        return subCombinations("", digits)

keymap = {}
keymap['2'] = ['a','b','c']
keymap['3'] = ['d','e','f']
keymap['4'] = ['g','h','i']
keymap['5'] = ['j','k','l']
keymap['6'] = ['m','n','o']
keymap['7'] = ['p','q','r','s']
keymap['8'] = ['t','u','v']
keymap['9'] = ['w','x','y','z']

def subCombinations(prefix, digits):
    nclist = keymap[digits[0]]
    
    digits = digits[1:]
    result = []
    for c in nclist:
        s = prefix + c
        if len(digits) == 0:
            result.append(s)
        else:
            result += subCombinations(s, digits)        
    
    return result        
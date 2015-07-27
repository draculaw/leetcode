class Solution:
    # @param {integer} n
    # @return {string[]}
    def generateParenthesis(self, n):
        if n == 0: return []
        if n == 1: return ["()"]

        return myGenerateParenthesis("", ["("]*n, [")"]*n, [])

def myGenerateParenthesis(prefix, llist, rlist, result):
    #print prefix, llist, rlist
    if len(llist) == 0:
        print prefix, llist, rlist
        return [prefix + "".join(rlist)]
    
        #prefix += "("
        #llist.pop()

    lresult = myGenerateParenthesis(prefix+"(", llist[1:], rlist, [])+result
    rresult = []
    if len(llist) < len(rlist):
        rresult = myGenerateParenthesis(prefix+")", llist, rlist[1:], [])+result  
        
        
    return lresult+rresult
        
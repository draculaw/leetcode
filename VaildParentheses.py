class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        match = {"{":"}", "(":")", "[":"]"}

        li = []
        sl = list(s)
        if len(sl) % 2: return False

        for c in sl:
            if len(li) != 0:
                try:
                    if match[li[-1]] == c:
                        li.pop()
                        continue
                except:
                    return False
            li.append(c)

        return len(li) == 0        
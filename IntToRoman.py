class Solution:
    # @param {integer} num
    # @return {string}
    def intToRoman(self, num):
        n = num
        RomanIntMap = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        RomanIntMap["CM"] = 900
        RomanIntMap["CD"] = 400
        RomanIntMap["XC"] = 90
        RomanIntMap["XL"] = 40
        RomanIntMap["IX"] = 9
        RomanIntMap["IV"] = 4

        newMap = sorted(RomanIntMap.items(), key=lambda d:d[1])[::-1]

        
        i = 0
        result = ""
        while (n > 0):
            b = newMap[i][1]
            c = n / b
            if c == 0:
                i += 1
                continue

            result += newMap[i][0] * c

            n = n % b
        
        return result        
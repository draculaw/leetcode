class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        if len(nums) == 0: return []
        if len(nums) == 1: return [str(nums[0])]
        r = []
        i = 0
        j = 0
        
        while len(nums) > 0:

            j = subRange(nums)
            
            k = j - 1
            if i != k:
                s = "->".join([str(nums[i]), str(nums[k])])
            else:
                s = str(nums[k])
            r.append(s)

            if j != len(nums):
                nums = nums[j:]
            else: break
            i = 0
            j = 0
            
            
        return r

def subRange(nums):
    
    i = 1
    for i in xrange(1, len(nums)):
    
        if nums[i] - nums[0] == i:
            i += 1
        else:  
    
            return i
    else:
        return i
    return 1        
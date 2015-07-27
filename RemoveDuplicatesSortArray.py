class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):

        l = len(nums) 
        if l < 2:
            return l 
        
        
        while l > 1:
            
            if nums[l - 1] == nums[l - 2]:
                del nums[l - 1]                
                
            l -= 1
            
        return len(nums)
        
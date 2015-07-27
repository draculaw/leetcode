class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        l = len(nums)
        if l < 2: return False
        if k < 1: return False

        if l <= k:
            return mycontainsDuplicate(nums)
            
        for i in xrange(l - k):
            if mycontainsDuplicate(nums[i:i + k + 1]):
                return True
        return False


           
def mycontainsDuplicate(nums):
    l = len(nums)
    if l == 0: return False
    
    nums = sorted(nums)

    for i in xrange(1,l):
        if nums[i - 1] == nums[i]: return True
            
    return False
        
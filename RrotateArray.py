class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        
        l = len(nums)
        new =  nums[l-k:]+nums[:l-k]
        for i in xrange(len(new)):
            nums[i]  = new[i]
            
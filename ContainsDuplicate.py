class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):

        l = len(nums)
        m = len(set(nums))

        return not l == m
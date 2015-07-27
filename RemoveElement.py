class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):

        new_num = [n for n in nums if n != val]

        for i in xrange(len(new_num)):
            nums[i] = new_num[i]

        return len(new_num)
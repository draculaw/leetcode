class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        
        r = nums[0]
        count = 0
        for n in nums[0:]:
            if r == n:
                count += 1
            else:
                count -= 1
                if count == 0:
                    r = n
                    count = 1

        return r
class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def threeSumClosest(self, nums, target):
        if len(nums) < 3: return None
        import math
        nums = sorted(nums)
        result = None

        found = False

        
        l = len(nums)
        for i in xrange(l):
            j = i + 1
            k = l - 1
            while (j < k):
                sumsum = nums[i] + nums[j] + nums[k]
                               

                if sumsum == target:
                    return sumsum

                if not found:
                    result = sumsum
                    found = True
                else:
                    if math.fabs(sumsum - target) < math.fabs(result - target):
                        result = sumsum
                if sumsum > target:
                    k -= 1
                else:
                    j += 1

        return result     

def myThreeSum(n, nums, results):
    
    i = 0
    j = len(nums) - 1
    
    while i < j:
        
        sumsum = n + nums[i] + nums[j]
        if sumsum < 0:
            i += 1 
        elif sumsum > 0:            
            j -= 1
        else:    
            result = [n, nums[i], nums[j]]
            if not result in results:
                results.append(result)
            i += 1 

    return results

    
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def threeSum(self, nums):
        nums = sorted(nums)

        results = []

        while len(nums) > 2 :            
        #if len(nums) > 3:
            #print nums
            n = nums[0]
            nums= nums[1:]

            results = myThreeSum(n, nums, results)
            
                                                     
        
        return results
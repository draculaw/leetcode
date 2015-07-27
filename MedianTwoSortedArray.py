def findkth(nums1, nums2, k):
    if len(nums1) > len(nums2):
        return findkth(nums2, nums1, k)

    if len(nums1) == 0:
        return nums2[k-1]
    if k == 1:
        return min(nums1[0], nums2[0])

    i = min (k/2, len(nums1))
    j = k - i

    if nums1[i-1] < nums2[j-1]:
        return findkth(nums1[i:], nums2, k-i)
    elif nums1[i-1] > nums2[j-1]:
        return findkth(nums1, nums2[j:], k-j)
    else:
        return nums1[i-1]
        
class Solution:
    # @param {integer[]} nums1
    # @param {integer[]} nums2
    # @return {float}
    def findMedianSortedArrays(self, nums1, nums2):
        
        
        l = len(nums1) + len(nums2)
        if l % 2:
            return findkth(nums1, nums2, l /2 + 1)
        else:
            return  (float)(findkth(nums1, nums2, l/2) + findkth(nums1,nums2, l/2 + 1)) /2
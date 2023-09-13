class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        c = nums1 + nums2
        c.sort()
        median = len(c) // 2
        if len(c) % 2 != 0:
            return c[median]
        else:
            return (c[median - 1] + c[median]) / 2

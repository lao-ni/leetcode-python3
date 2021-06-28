class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #print(set(nums1))
        return set(nums1)&set(nums2)

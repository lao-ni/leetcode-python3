class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1)<len(nums2):
            hashmap=collections.Counter(nums1)
            num=nums2
        else:
            hashmap=collections.Counter(nums2)
            num=nums1
        #print(hashmap)
        ans=[]
        for n in num:
            if hashmap[n]>0:
                ans.append(n)
                hashmap[n]=hashmap[n]-1
        return ans

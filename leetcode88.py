class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        point1=m-1
        point2=n-1
        loc=n+m-1
        if len(nums1)==1 and len(nums2)==1:
            nums1[0]=nums2[0]
            
        else:
            while point2>=0 and point1>=0:
                
                if nums1[point1]>nums2[point2]:
                    nums1[loc]=nums1[point1]
                    point1-=1
                    loc-=1
                else:
                    
                    nums1[loc]=nums2[point2]
                    point2-=1
                    
                    loc-=1
                
            if point1==-1 and point2!=-1:
                nums1[0:point2+1]=nums2[0:point2+1]
        
                

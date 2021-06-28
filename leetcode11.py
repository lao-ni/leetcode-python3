class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        maxarea=0
        while i !=j:
            if height[i]<=height[j]:
                area=height[i]*(j-i)
                if area>maxarea:
                    maxarea=area
                i+=1
            else:
                area=height[j]*(j-i)
                if area>maxarea:
                    maxarea=area
                j-=1
        return maxarea


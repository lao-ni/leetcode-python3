class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans=nums[0]

        curr_sum=nums[0]
        for i in range(1,len(nums)):
            if curr_sum<0:
                curr_sum=nums[i]
                
            else:
                
                curr_sum=nums[i]+curr_sum
            if curr_sum>ans:
                ans=curr_sum
            
        return ans
                

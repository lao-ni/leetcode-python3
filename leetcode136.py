class Solution:
    def singleNumber(self, nums: List[int]) -> int:
       # return sum(set(nums))*2-sum(nums)  #a mathmatical method
       a=0
       for i in nums:
           a=a^i
       return a


class Solution:
    def massage(self, nums: List[int]) -> int:
        if nums==[]:
            return 0
        else:
            for i in range(len(nums)):
                if i==0:
                    continue
                elif i==1:
                    nums[i]=max(nums[0],nums[1])
                else:
                    nums[i]=max(nums[i-1],nums[i]+nums[i-2])
        return nums[i]

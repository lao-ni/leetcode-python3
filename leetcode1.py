class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for ind,num in enumerate(nums):
            hashmap[num]=ind
        for i,num1 in enumerate(nums):
            j=hashmap.get(target-num1)
            if j is not None and j!=i:
                return[i,j]

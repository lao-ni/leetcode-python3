class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        cur=gas[0]-cost[0]
        res=0
        min=cur
        if sum(gas)<sum(cost):
            return -1
        else:
            for i in range(1,len(gas)):
                cur=cur+gas[i]-cost[i]
                if cur<min:
                    min=cur
                    res=i
            if res==len(gas)-1:
                return 0
            else:
                return res+1
                


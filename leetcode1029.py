class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cost_change=[c[0]-c[1] for c in costs]
        cost_change.sort()
        n=len(costs)//2
        b=0
        for i in range(len(costs)):
            b=b+costs[i][1]
        for i in range(n):
            b=b+ cost_change[i]
        return b

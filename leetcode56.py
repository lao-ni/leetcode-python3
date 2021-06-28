class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        ans=[]
        left=intervals[0][0]
        right=intervals[0][1]
        for i in range(len(intervals)):
            if intervals[i][0]<=right:
                right=max(right,intervals[i][1])
                if i==len(intervals)-1:
                    ans.append([left,right])
            else:#两区间没有交集
                ans.append([left,right])
                left=intervals[i][0]
                right=intervals[i][1]
                if  i==len(intervals)-1:
                    ans.append(intervals[-1])

            
        return ans

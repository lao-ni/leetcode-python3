class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        count=0
        for j in range(len(A[0])):
            for i in range(1,len(A)):
                if A[i][j]<A[i-1][j]:
                    count=count+1
                    break
        return count


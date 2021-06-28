class Solution:
    def hammingWeight(self, n: int) -> int:
        n=str(bin(n))
        #print(n)
        count=0
        for i in range(len(n)):
            #print(n[i])
            if n[i]=='1':
                count+=1
        
        return count

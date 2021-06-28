class Solution:
    def countPrimes(self, n: int) -> int:
        
        if n==0 or n==1 or n==2:
            return 0
        else:
            isPrime=[1]*n
            isPrime[0]=0
            isPrime[1]=0
            for i in range(2,int(n**0.5)+1):
                if isPrime[i]==1:
                    j=i
                    while i*j<n:
                        isPrime[i*j]=0
                        j+=1
            #print(isPrime)
            return sum(isPrime)


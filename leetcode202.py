class Solution:
    def isHappy(self, n: int) -> bool:
        def getNext(n):
            res=0
            while n >0:
                n,digit=divmod(n,10)
                res=res+digit**2
            return res
        numset=set()
        while True:
            #print(numset,getNext(n))
            if getNext(n) in numset:
                #print(numset,getNext(n))
                return False
            else:
                if getNext(n)==1:
                    return True
                else:
                    numset.add(getNext(n))
                    n=getNext(n)

            
            

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a)>len(b):
            b=b.rjust(len(a),'0')
        elif len(b)>len(a):
            a=a.rjust(len(b),'0')
        b=b[::-1]
        a=a[::-1]
        jinwei=0
        result=''
        for i in range(len(a)):
            if int(a[i])+int(b[i])+jinwei==0:
            #if int(a[i])+int(b[i])+jinwei==0：
                result=result+'0'
                jinwei=0
            elif int(a[i])+int(b[i])+jinwei==1:
                result=result+'1'
                jinwei=0
            elif int(a[i])+int(b[i])+jinwei==2:
                result=result+'0'
                jinwei=1
            elif int(a[i])+int(b[i])+jinwei==3:
                result=result+'1'
                jinwei=1
        if jinwei==1:
            result=result+'1'
        return result[::-1]

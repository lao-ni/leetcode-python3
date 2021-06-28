class Solution:
    def decodeString(self, s: str) -> str:
        n=0 
        stack=[]
        res=''
        for c in s:
            if c.isdigit():
                n=n*10+int(c)
            elif c.isalpha():
                res=res+c
            elif c=='[':
                stack.append([n,res])
                res=''
                n=0
            elif c==']':
                x,y=stack.pop()
                res=y+x*res
        return res

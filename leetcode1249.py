class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        count=0
        for i in range(len(s)):
            if s[i]=='(':
                count=count+1
                stack.append(s[i])
            elif s[i]==')':
                count=count-1
                if count>=0:
                    stack.append(s[i])
                elif count<0:
                    count=0
            else:
                stack.append(s[i])
        s=''.join(stack)
        stack2=[]
        count=0
        #print(s)
        for i in range(len(s)-1,-1,-1):
            
            if s[i]=='(':
                count=count+1
                if count<=0:
                    stack2.append(s[i])
                elif count>0:
                    count=0
            elif s[i]==')':
                count=count-1
                stack2.append(s[i])
            else:
                stack2.append(s[i])
        return ''.join(stack2)[::-1]

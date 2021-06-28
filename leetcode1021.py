class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        stack=[]
        num=0
        s=''
        for i in range(len(S)):
            if S[i]=='(':
                num=num+1
                
                if num==0 and stack:
                    stack.pop(0)
                    s=s+''.join(stack)
                    stack=[]
                else:
                    stack.append(S[i])
                #print(num,stack)
            if S[i]==')':
                num=num-1
                if num==0 and stack:
                    stack.pop(0)
                    s=s+''.join(stack)
                    stack=[]
                else:
                    stack.append(S[i])
                #print(num,stack)
        return s

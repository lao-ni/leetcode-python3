class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack=[]
        
        for i in range(0,len(S)):
            if stack==[]:
                stack.append(S[i])
            elif S[i]==stack[-1]:
                stack.pop()
            else:
                stack.append(S[i])
        return ''.join(stack)



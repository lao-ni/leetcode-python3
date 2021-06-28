class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack=[0]
        for c in S:
            if c=='(':
                
                stack.append(0)
                #print(stack)
            else:
                
                if stack[-1]==0:
                    stack[-2]=1+stack[-2]
                else:
                    stack[-2]=stack[-1]*2+stack[-2]
                stack.pop()
                #print(stack)
        return stack[0]

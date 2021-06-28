class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        l=['+','-','*','/']
        for i  in range(len(tokens)):
            if tokens[i] in l:
                a=int(stack.pop())
                b=int(stack.pop())
                if tokens[i]=='+':
                    stack.append(a+b)
                    #print(stack)
                elif tokens[i]=='*':
                    stack.append(a*b)
                    #print(stack) 
                elif tokens[i]=='-':
                    stack.append(b-a)
                    #print(stack)
                elif tokens[i]=='/':
                    stack.append(int(b/a))
                    #print(stack)
            else:
                stack.append(tokens[i])
        
        return int(stack[-1])

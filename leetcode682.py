class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack=[]
        for i in range(len(ops)):
            if ops[i]=='C':
                stack.pop()
                #print(stack)
            elif ops[i]=='D':
                stack.append(int(stack[-1])*2)
                #print(stack)
            elif ops[i]=='+':
                stack.append(int(stack[-1])+int(stack[-2]))
                #print(stack)
            else:
                stack.append(int(ops[i]))
                #print(stack)
        return sum(stack)

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack_s=[]
        stack_t=[]
        for i in range(len(S)):
            if stack_s and S[i]=='#':
                stack_s.pop()
            elif S[i]=='#':
                pass
            else:
                stack_s.append(S[i])
        for i in range(len(T)):
            if stack_t and T[i]=='#':
                stack_t.pop()
            elif T[i]=='#':
                pass
            else:
                stack_t.append(T[i])
        return stack_s==stack_t


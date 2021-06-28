class Solution:
    def isValid(self, s: str) -> bool:
        if s=='':
            return True
        else:
            l=[]
            for i in range(len(s)):
                if s[i]=='('or s[i]=='[' or  s[i]=='{':
                    l.append(s[i])
                else:
                    if s[i]==')':
                        if l!=[] and l[-1]=='(':
                            l.pop()
                        else:
                            return False
                    elif s[i]==']':
                        if l!=[] and l[-1]=='[':
                            l.pop()
                        else:
                            return False
                    else:
                        if l!=[] and l[-1]=='{':
                            l.pop()
                        else:
                            return False
            if l==[]:
                return True
            else:
                return False

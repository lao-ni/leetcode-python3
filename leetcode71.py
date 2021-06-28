class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.strip("/").split("/")
        stack=[]
        for i in range(len(path)):
            if path[i]=='..':
                if stack:
                    stack.pop()
            elif path[i]=='.' or path[i]=='':
                pass
            else:
                stack.append(path[i])
        return '/'+'/'.join(stack)


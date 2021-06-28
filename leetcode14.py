class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs==[]:
            return ''
        else:
            for j in range(len(strs[0])):
                for i in range(len(strs)):
                    if len(strs[i])==j:
                        return strs[0][0:j]
                    elif strs[i][j]!=strs[0][j]:
                        return strs[0][0:j]
                    else:
                        continue
            return strs[0]

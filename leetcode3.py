class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s=="":
            return 0
        elif s==" ":
            return 1
        else:
            i=0
            max=0
            window=[]
            for j in range(0,len(s)):
                if s[j] not in window: #如果无重复字符就直接加入滑动窗口
                    window.append(s[j])
                    if len(window)>max:
                        max=len(window)
                    print(window)
                elif s[j] in window: 
                    #如果有重复字符就从重复字符下一位开始重新建立一个滑动窗口
                    c=window.index(s[j])
                    window=list(s[i+c+1:j+1])
                    i=i+c+1
                    print(window)
            return max

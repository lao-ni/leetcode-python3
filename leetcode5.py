class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxans=''
        if len(s)==1:
            return s
        else:
            new_s=''
            for i in range(len(s)):
                new_s=new_s+s[i]+'#'
            #print(new_s)
            for i in range(1,len(new_s)-1):
                step=1
                ans=''          
                while i-step>=0 and i+step<=len(new_s)-1:
                    if new_s[i-step]==new_s[i+step]:
                        ans=new_s[i-step:i+step+1]
                        step=step+1
                        if len(ans)>len(maxans):
                            maxans=ans
                    else:
                        break
                        if len(ans)>len(maxans):
                            maxans=ans
            a=''
            for i in range(len(maxans)):
                if maxans[i]!='#':
                    a=a+maxans[i]
            return a




        

            

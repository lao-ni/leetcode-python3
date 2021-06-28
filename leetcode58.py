class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count=0
    
        if s==" ":
            return 0
        else:
            for i in range(len(s)-1,-1,-1):
                if count==0:
                    if s[i]==" ":
                        continue
                    else:
                        count=1
                else:
                    if s[i]==" ":
                        break
                    else:
                        count=count+1
        return count

                    
            

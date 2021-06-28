class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s):
            if len(s)==1:
                return True
            else:
                if s==s[::-1]:
                    return True 
                else:
                    return False

        low=0
        high=len(s)-1
        if isPalindrome(s)==True:
            return True
        while low<high:
            if s[low]!=s[high]:
                return isPalindrome(s[low+1:high+1]) or isPalindrome(s[low:high])
            else:
                low+=1
                high-=1
        return True
        
            

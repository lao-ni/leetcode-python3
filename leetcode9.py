class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        elif x<10:
            return True
        
        else:
           if str(x)==str(x)[::-1]:
               return True
        return False

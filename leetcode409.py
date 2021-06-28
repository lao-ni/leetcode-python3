class Solution:
    def longestPalindrome(self, s: str) -> int:
        count=collections.Counter(s)
        res=0
        for c in count.values():
            res=res+c//2*2
            if c%2!=0 and res%2==0:
                res=res+1
        return res 

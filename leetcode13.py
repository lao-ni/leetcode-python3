class Solution:
    def romanToInt(self, s: str) -> int:
        res=0
        hashmap= {'I':1,'V':5, 'X':10,  'L':50,  'C':100,  'D':500,  'M':1000}
        for i in range(len(s)-1):
            if hashmap.get(s[i])<hashmap.get(s[i+1]):
                res=res-2*hashmap.get(s[i])
                #print(s[i],s[i-1],res)
            res=res+hashmap.get(s[i])
        return res+hashmap.get(s[-1])

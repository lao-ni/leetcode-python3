class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            return int(str(x)[::-1]) if int(str(x)[::-1])<=2147483648 else 0
        else:
            return int('-'+str(x)[:0:-1]) if int('-'+str(x)[:0:-1])>=-2147483648 else 0

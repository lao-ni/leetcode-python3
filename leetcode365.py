class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        n=math.gcd(x,y)
        if x+y<z:
            return False
        if x==0 or y==0:
            return z==0 or z==x+y
        return z%n==0

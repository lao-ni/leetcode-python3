from fractions import gcd
from collections import Counter
from functools import reduce
class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        a=Counter(deck).values()
        return reduce(gcd,a)>1


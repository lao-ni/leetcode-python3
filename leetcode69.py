class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        else:
            guess=10
            new_guess=0.5*(guess+x/guess)
            while abs(guess-new_guess)>1e-6:
                #print(guess,new_guess)
                guess=new_guess
                new_guess=0.5*(guess+x/guess)
        #print
        return int(new_guess)

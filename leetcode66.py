class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]!=9:
            digits[-1]=digits[-1]+1
            return digits
        else:
            digits=digits[::-1]
            for i in range(len(digits)):
                if digits[i]!=9:
                    digits[i]=digits[i]+1
                    for j in range(i):
                        digits[j]=0
                    break
                if i==len(digits)-1:
                    for j in range(len(digits)):
                        digits[j]=0
                    digits.append(1)

            return digits[::-1]


        


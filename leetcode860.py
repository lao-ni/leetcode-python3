class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five=0
        ten=0
        twenty=0
        for i in range(len(bills)):
            if bills[i]==5:
                five=five+1
            elif bills[i]==10:
                if five!=0:
                    five=five-1
                    ten=ten+1
                else:
                    return False
                    break
            elif bills[i]==20:
                if ten!=0 and five!=0:
                    ten=ten-1
                    five=five-1
                    twenty+=1
                elif ten==0 and five>2:
                    five=five-3
                    twenty=twenty+1
                else:
                    return False
                    break
        
        return True
        

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        else:
            ans=0
            buy=prices[0]
            sell=prices[0]
            for i in range(1,len(prices)):
                if prices[i]>sell:
                    sell=prices[i]
                   
                elif prices[i]<buy:
                    
                    if sell-buy>ans:
                        ans=sell-buy
                    buy=prices[i]
                    sell=prices[i]
                    
            return max(ans,sell-buy)

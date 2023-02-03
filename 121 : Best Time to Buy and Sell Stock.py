class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        day1 = prices[0]
        profit = 0
        for i in range(1,len(prices)):
            if prices[i]>day1:
                profit = max(profit,prices[i]-day1)
            day1 = min(day1,prices[i])
        
        return profit

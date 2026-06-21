class Solution:
    def maxProfit(self, prices: List[int]) -> int:


        opt = []

        max_profit = 0
        min_price = float('inf')
        i = 0
        while i < len(prices):
            min_price = min(min_price, prices[i])

            profit = prices[i] - min_price

            max_profit = max(profit, max_profit)

            i+=1
        
        return max_profit

        
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = r = 0
        max_profit = 0
        
        for i, p in enumerate(prices):
            if p < prices[l]:
                r = l = i
            if p > prices[r]:
                r = i
            if l < r:
                max_profit = max(max_profit, prices[r] - prices[l])
        
        return max_profit

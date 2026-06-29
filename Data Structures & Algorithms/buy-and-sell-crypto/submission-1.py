class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minPrice = 101
        for p in prices:
            minPrice = min(minPrice, p)
            if p - minPrice > maxProfit:
                maxProfit = p - minPrice
            
        return maxProfit
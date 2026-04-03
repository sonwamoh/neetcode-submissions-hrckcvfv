class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        [10 1 1 1 1 1]
        [0  0 4 5 6 0]
        """
        min_price = float('inf')
        max_profit = float('-inf')

        for n in prices:
            min_price = min(min_price, n)
            max_profit = max(max_profit, n - min_price)
        
        return max_profit

        
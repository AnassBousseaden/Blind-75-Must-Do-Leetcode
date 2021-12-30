class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        bestScore = 0
        mini = prices[0]
        for sellingPrice in prices:
            mini = min(mini, sellingPrice)
            bestScore = max(bestScore, sellingPrice-mini)
        return bestScore


test = Solution()

prices = [7, 1, 5, 3, 6, 4]

print(test.maxProfit(prices))

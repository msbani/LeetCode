class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1 or k == 0:
            return 0

        if k >= n //2:
            return sum(
                max(0, prices[i] - prices[i - 1])
                for i in range(1, n)
            )

        buys = [-float('inf')] * (k + 1)
        sells = [0] * (k + 1)

        for price in prices:
            for j in range(1, k + 1):
                buys[j] = max(buys[j], sells[j-1] - price)
                sells[j] = max(sells[j], buys[j] + price)

        return sells[k]
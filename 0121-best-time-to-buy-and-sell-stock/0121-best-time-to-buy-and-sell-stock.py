
class Solution:
    def maxProfit(self, prices: List[int])-> int:

        # buy = prices[0]
        # profit = 0

        # for i in range(1, len(prices)):
        #     if prices[i] < buy:
        #         buy = prices[i]
        #     elif prices[i] - buy > profit:
        #         profit = prices[i] - buy

        # return profit

# Another solution(Two Pointer)

        # l, r = 0, 1
        # maxP = 0

        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         profit = prices[r] - prices[l]
        #         maxP = max(profit, maxP)
        #     else:
        #         l = r
        #     r += 1

        # return maxP

        profit = 0
        buy = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[buy]:
                profit = max(profit, prices[i] - prices[buy])
            else:
                buy = i
        return profit

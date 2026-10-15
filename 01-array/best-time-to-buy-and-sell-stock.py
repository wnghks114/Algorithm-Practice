prices = list(map(int, input().split()))

min_price = prices[0]
max_profit = 0

for price in prices[1:] :
    profit = price - min_price
    max_profit = max(max_profit, profit)
    min_price = min(min_price, price)

print(max_profit)

## leetcode version submission 

class Solution(object):
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0

        for price in prices[1:] :
            profit = price - min_price
            max_profit = max(max_profit, profit)
            min_price = min(min_price, price)

        return max_profit
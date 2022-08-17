"""
Problem : Best time to buy and sell

Problem description : We have an array for which nth element is the price of given stock on day n.
If we were only permitted to buy one share and sell one share of stock. Design an algorithm to find
Max profit. Note we cannot sell a stock before buying one.

Key method : Arrays and Array operations and using pointers (language specific)

General tip : Buy low, Sell high, Maximise the profit.

Example 1

Input = [7, 1, 5, 3, 6, 4]
Output = 5

Explanation : Buy on day[2] where the price is '1' and sell on day[5] where the price is '6'.
Profit = 6 - 1 = 5. Selling price should be always higher than buying price to yield profit.
Find which day gives the max profit. Also remember we cannot go back in time to sell; as time
always is in one direction. We cannot buy on day[2] and sell on day[1] as the price is '7' here
we are going back in time which is not allowed in reality.

"""


class ProblemOneSolution:

    def bestDayToSell(self, prices: list[int]) -> int:
        left, right = 0, 1  # left=Buy, right=Sell
        maxProfit = 0   # this will change as we itter in following code
        # Run the loop till the end of list length
        while right < len(prices):
            # check profitability
            # If price of left(buying) element is smaller than right(selling)
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]  # Profit is always when selling price is higher than buying.
                maxProfit = max(maxProfit, profit)  # Compare the profit to maxProfit to get maxProfit value
            # If there is no profit in the transaction
            else:
                left = right
            right += 1
        return maxProfit


problem = ProblemOneSolution()
solution = problem.bestDayToSell([7, 1, 5, 3, 6, 4])
print(solution)

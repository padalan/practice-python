"""
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.

Constraints:

    1 <= prices.length <= 105
    0 <= prices[i] <= 104

"""

class Solution():
  def maxProfit(self, prices):
      # Initialize variables
      min_price = float('inf')  # Start with a very large number
      max_profit = 0            # Start with 0 profit

      # Loop through each price in the list
      for price in prices:
          # Update the minimum price if the current price is lower
          if price < min_price:
              min_price = price
          # Calculate the potential profit
          current_profit = price - min_price
          # Update max_profit if the current_profit is higher
          if current_profit > max_profit:
              max_profit = current_profit

      # Return the maximum profit achieved
      return max_profit

# Test cases
sol = Solution()
print(sol.maxProfit([7, 1, 5, 3, 6, 4]))  # Output: 5 (buy on day 2, sell on day 5)
print(sol.maxProfit([7, 6, 4, 3, 1]))     # Output: 0 (no transaction is done)


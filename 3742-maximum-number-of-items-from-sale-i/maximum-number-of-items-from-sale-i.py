from typing import List


class Solution:

  def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
    dp = [0] * (budget + 1)
    min_price = float("inf")

    for factor_i, price_i in items:
      min_price = min(min_price, price_i)

      # Count 1 (the item itself) + all other items divisible by factor_i
      gain = sum(1 for factor_j, _ in items if factor_j % factor_i == 0)

      # 0/1 Knapsack transition (iterate backwards)
      for w in range(budget, price_i - 1, -1):
        dp[w] = max(dp[w], dp[w - price_i] + gain)

    # Combine first-purchase gains with greedy spending of remaining budget
    max_items = 0
    for w in range(budget + 1):
      extra_copies = (budget - w) // min_price
      max_items = max(max_items, dp[w] + extra_copies)

    return max_items

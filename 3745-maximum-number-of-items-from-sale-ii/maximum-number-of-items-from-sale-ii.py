from typing import List


class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        min_price = min(price for _, price in items)

        factor_cnt = [0] * (n + 1)
        for factor, _ in items:
            factor_cnt[factor] += 1

        multiples_cnt = [0] * (n + 1)
        for f in range(1, n + 1):
            if factor_cnt[f]:
                for mult in range(f, n + 1, f):
                    multiples_cnt[f] += factor_cnt[mult]

        deals = []
        for factor, price in items:
            gain = multiples_cnt[factor] - 1
            if gain > 0 and price < 2 * min_price:
                deals.append((price, gain))

        deals.sort(key=lambda x: x[0])

        total = 0
        rem = budget
        for price, gain in deals:
            if rem < price:
                break
            take = min(gain, rem // price)
            total += 2 * take
            rem -= take * price

        total += rem // min_price
        return total

import random
from collections import Counter
from typing import List


class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        mod1, mod2 = 1_000_000_007, 1_000_000_009
        base1 = random.randint(100_000_000, 900_000_000)
        base2 = random.randint(100_000_000, 900_000_000)
        offset = 1_000_000_007

        pow1 = [1] * (n + 1)
        pow2 = [1] * (n + 1)
        pref1 = [0] * (n + 1)
        pref2 = [0] * (n + 1)

        for i, val in enumerate(nums):
            x = val + offset
            pow1[i + 1] = (pow1[i] * base1) % mod1
            pow2[i + 1] = (pow2[i] * base2) % mod2
            pref1[i + 1] = (pref1[i] * base1 + x) % mod1
            pref2[i + 1] = (pref2[i] * base2 + x) % mod2

        def has_unique(length: int) -> bool:
            counts = Counter()
            for start in range(n - length + 1):
                end = start + length
                h1 = (pref1[end] - pref1[start] * pow1[length]) % mod1
                h2 = (pref2[end] - pref2[start] * pow2[length]) % mod2
                counts[(h1, h2)] += 1
            return any(cnt == 1 for cnt in counts.values())

        lo, hi = 1, n
        ans = n
        while lo <= hi:
            mid = (lo + hi) // 2
            if has_unique(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return ans

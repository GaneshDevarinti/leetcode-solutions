class Solution:

  def minMoves(self, nums: list[int]) -> int:
    mx = max(nums)
    n = len(nums)
    total_sum = sum(nums)
    return (mx * n) - total_sum

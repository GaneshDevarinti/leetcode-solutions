class Solution:
    def minMoves(self, nums: list[int]) -> int:
        """
        Calculates the minimum moves to make all elements equal.
        Time Complexity: O(n) | Space Complexity: O(1)
        """
        return sum(nums) - len(nums) * min(nums)

class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        # Convert each number to its squared value
        squares = [x * x for x in nums]
        
        # Sort squares in ascending order
        squares.sort()
        
        n = len(nums)
        # The first n // 2 elements will be subtracted
        # The remaining elements will be added
        ans = sum(squares[n // 2:]) - sum(squares[:n // 2])
        
        return ans

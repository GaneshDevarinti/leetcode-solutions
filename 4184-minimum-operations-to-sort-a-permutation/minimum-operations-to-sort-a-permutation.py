class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        idx = nums.index(0)
        
        # Check if the array is an increasing cyclic rotation from 0
        is_increasing = True
        for i in range(n):
            if nums[(idx + i) % n] != i:
                is_increasing = False
                break
                
        # Check if the array is a decreasing cyclic rotation from 0
        is_decreasing = True
        for i in range(n):
            if nums[(idx - i + n) % n] != i:
                is_decreasing = False
                break
        
        # Calculate minimum cost
        ans = float('inf')
        if is_increasing:
            ans = min(ans, idx, 2 + n - idx)
        if is_decreasing:
            ans = min(ans, n - idx, idx + 2)
            
        return ans if ans != float('inf') else -1

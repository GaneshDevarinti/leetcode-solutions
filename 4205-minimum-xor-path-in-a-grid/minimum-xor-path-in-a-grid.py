class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        MAX_XOR = 1024
        
        # dp[j] will store the set of possible XOR values for column j in the current row
        dp = [set() for _ in range(n)]
        
        # Base case: Starting point
        dp[0].add(grid[0][0])
        
        # Initialize the first row (can only move right)
        for j in range(1, n):
            for val in dp[j - 1]:
                dp[j].add(val ^ grid[0][j])
                
        # Fill the rest of the grid row by row
        for i in range(1, m):
            new_dp = [set() for _ in range(n)]
            
            # First cell of the current row (can only move down from previous row)
            for val in dp[0]:
                new_dp[0].add(val ^ grid[i][0])
                
            # Rest of the cells in the current row (can come from above or left)
            for j in range(1, n):
                current_val = grid[i][j]
                
                # From above (dp[j])
                for val in dp[j]:
                    new_dp[j].add(val ^ current_val)
                    
                # From the left (new_dp[j-1])
                for val in new_dp[j - 1]:
                    new_dp[j].add(val ^ current_val)
                    
            dp = new_dp
            
        # The answer is the smallest possible XOR value at the destination cell
        return min(dp[n - 1])

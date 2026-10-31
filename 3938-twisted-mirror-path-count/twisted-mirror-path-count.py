from typing import List
from functools import lru_cache

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        MOD = 10**9 + 7
        
        # Helper function to trace chain reflections through consecutive mirrors
        def reflect(r, c, direction):
            while 0 <= r < ROW and 0 <= c < COL and grid[r][c] == 1:
                if direction == 'right':
                    r += 1
                    direction = 'down'
                else:
                    c += 1
                    direction = 'right'
            return (r, c)
            
        @lru_cache(None)
        def dp(r, c):
            # If out of bounds or starting on/landing directly on a mirror, invalid path
            if not (0 <= r < ROW and 0 <= c < COL) or grid[r][c] == 1:
                return 0
            
            # Reached target corner
            if (r, c) == (ROW - 1, COL - 1):
                return 1
                
            total = 0
            
            # --- Option 1: Move Right ---
            nR, nC = r, c + 1
            if 0 <= nC < COL:
                if grid[nR][nC] == 0:
                    total += dp(nR, nC)
                else:
                    # Hits a mirror moving right -> turned DOWN to the cell below it
                    reflectR, reflectC = reflect(nR + 1, nC, 'down')
                    total += dp(reflectR, reflectC)
                    
            # --- Option 2: Move Down ---
            nR, nC = r + 1, c
            if 0 <= nR < ROW:
                if grid[nR][nC] == 0:
                    total += dp(nR, nC)
                else:
                    # Hits a mirror moving down -> turned RIGHT to the cell right of it
                    reflectR, reflectC = reflect(nR, nC + 1, 'right')
                    total += dp(reflectR, reflectC)
                    
            return total % MOD
            
        return dp(0, 0)

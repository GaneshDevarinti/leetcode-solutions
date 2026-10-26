class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        island_count = 0
        
        # Iterative DFS using an explicit stack to avoid recursion stack overflow
        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    island_sum = 0
                    stack = [(r, c)]
                    
                    # Accumulate the value of the current cell and sink it
                    island_sum += grid[r][c]
                    grid[r][c] = 0 
                    
                    while stack:
                        curr_r, curr_c = stack.pop()
                        
                        # Explore 4-directional neighbors
                        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nr, nc = curr_r + dr, curr_c + dc
                            
                            # Check boundaries and if the neighbor is an unvisited land cell
                            if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                                island_sum += grid[nr][nc]
                                grid[nr][nc] = 0  # Mark as visited
                                stack.append((nr, nc))
                                
                    # Verify if the total island value is divisible by k
                    if island_sum % k == 0:
                        island_count += 1
                        
        return island_count

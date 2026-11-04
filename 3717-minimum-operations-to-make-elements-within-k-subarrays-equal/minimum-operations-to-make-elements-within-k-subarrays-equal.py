from sortedcontainers import SortedList

class Solution:
    def minOperations(self, nums: list[int], x: int, k: int) -> int:
        n = len(nums)
        
        # Step 1: Compute the L1 cost to make each window of size x equal to its median
        window_costs = [0] * (n - x + 1)
        
        # We will split the window into two halves to calculate the absolute differences efficiently
        left_half = SortedList()   # Holds the smaller half of the elements
        right_half = SortedList()  # Holds the larger half of the elements
        left_sum = 0
        right_sum = 0
        
        def add_num(val):
            nonlocal left_sum, right_sum
            # Insert into the appropriate half
            if not left_half or val <= left_half[-1]:
                left_half.add(val)
                left_sum += val
            else:
                right_half.add(val)
                right_sum += val
            balance()

        def remove_num(val):
            nonlocal left_sum, right_sum
            # Remove from the appropriate half
            if val <= left_half[-1] and val in left_half:
                left_half.remove(val)
                left_sum -= val
            else:
                right_half.remove(val)
                right_sum -= val
            balance()

        def balance():
            nonlocal left_sum, right_sum
            # Maintain the size property: len(left_half) == len(right_half) (+1 if odd)
            while len(left_half) > len(right_half) + 1:
                moved = left_half.pop(-1)
                left_sum -= moved
                right_half.add(moved)
                right_sum += moved
            while len(left_half) < len(right_half):
                moved = right_half.pop(0)
                right_sum -= moved
                left_half.add(moved)
                left_sum += moved

        # Initialize the first window
        for i in range(x):
            add_num(nums[i])
            
        # The median is always the maximum element of the left half
        median = left_half[-1]
        window_costs[0] = (len(left_half) * median - left_sum) + (right_sum - len(right_half) * median)
        
        # Slide the window across the rest of the array
        for i in range(x, n):
            remove_num(nums[i - x])
            add_num(nums[i])
            median = left_half[-1]
            window_costs[i - x + 1] = (len(left_half) * median - left_sum) + (right_sum - len(right_half) * median)
            
        # Step 2: Dynamic Programming to pick k non-overlapping windows
        # dp[i][j] = min cost to pick j windows from the suffix starting at index i
        inf = float('inf')
        dp = [[inf] * (k + 1) for _ in range(n + 1)]
        
        # Base case: 0 windows needed costs 0
        for i in range(n + 1):
            dp[i][0] = 0
            
        for i in range(n - 1, -1, -1):
            for j in range(1, k + 1):
                # Option 1: Skip the current index
                dp[i][j] = dp[i + 1][j]
                
                # Option 2: Take the window starting at index i (if it fits)
                if i + x <= n and window_costs[i] != inf:
                    take_cost = window_costs[i] + dp[i + x][j - 1]
                    if take_cost < dp[i][j]:
                        dp[i][j] = take_cost
                        
        return dp[0][k]

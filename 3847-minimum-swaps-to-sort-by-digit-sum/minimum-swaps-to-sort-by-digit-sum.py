class Solution:
    def minSwaps(self, nums: list[int]) -> int:
        def get_digit_sum(n: int) -> int:
            s = 0
            while n > 0:
                s += n % 10
                n //= 10
            return s
        
        # 1. Sort a copy of the numbers based on (digit_sum, value)
        sorted_nums = sorted(nums, key=lambda x: (get_digit_sum(x), x))
        
        # 2. Map each distinct number to its destination index
        target_index = {num: i for i, num in enumerate(sorted_nums)}
        
        # 3. Use Cycle Decomposition to count the swaps
        visited = [False] * len(nums)
        swaps = 0
        
        for i in range(len(nums)):
            # If already processed or already in the correct spot, skip
            if visited[i] or target_index[nums[i]] == i:
                continue
            
            # Trace the cycle size
            cycle_size = 0
            curr_idx = i
            while not visited[curr_idx]:
                visited[curr_idx] = True
                curr_idx = target_index[nums[curr_idx]]
                cycle_size += 1
            
            # A cycle of length k requires k - 1 swaps
            if cycle_size > 0:
                swaps += (cycle_size - 1)
                
        return swaps

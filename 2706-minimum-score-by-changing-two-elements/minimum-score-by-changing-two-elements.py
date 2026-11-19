from typing import List

class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        nums.sort()
        
        # Option 1: Change the two smallest elements (nums[0], nums[1])
        change_two_smallest = nums[-1] - nums[2]
        
        # Option 2: Change the two largest elements (nums[-1], nums[-2])
        change_two_largest = nums[-3] - nums[0]
        
        # Option 3: Change one smallest (nums[0]) and one largest (nums[-1])
        change_one_each = nums[-2] - nums[1]
        
        return min(change_two_smallest, change_two_largest, change_one_each)

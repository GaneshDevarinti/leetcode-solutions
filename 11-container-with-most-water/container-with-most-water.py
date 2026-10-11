class Solution:
    def maxArea(self, height: list[int]) -> int:
        left=0
        right=len(height)-1
        max_water=0
        while left<right:
            water=min(height[left],height[right])*(right-left)
            max_water=max(max_water,water)
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_water

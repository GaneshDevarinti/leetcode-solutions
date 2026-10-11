class Solution {
    public int maxArea(int[] height) {
        int l=0;
        int r=height.length-1;
        int maxw=0;
        while(l<r){
            int water=Math.min(height[l],height[r])*(r-l);
            maxw=Math.max(maxw,water);
            if(height[l]<height[r]){
                l++;
            }
            else{
                r--;
            }
        }
        return maxw;
        
    }
}
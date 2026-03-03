class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        maxWater = 0

        while l<r:
            width = r - l
            heights = min(height[l],height[r])
            area = heights * width

            maxWater = max(maxWater, area)
            
            if height[l] < height[r]:
                l+=1
            else:
                r-=1
        return maxWater
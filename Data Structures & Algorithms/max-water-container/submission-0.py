class Solution:
    def maxArea(self, heights: List[int]) -> int:
        r = len(heights) - 1
        l = 0
        max_water = 0
        
        while r > l:
            water = min(heights[r], heights[l]) * (r - l)
            max_water = max(max_water, water)
            
            if heights[r] < heights[l]:
                r -= 1
            else:
                l += 1

        return max_water


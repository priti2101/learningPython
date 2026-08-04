class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height)-1
        max_water=0  

        while left<right:
            current_area = (right-left)*min(height[left], height[right])
            max_water = max(max_water, current_area)

            if height[left] < height[right]:
               left += 1
            else:
               right -= 1

        return max_water
        
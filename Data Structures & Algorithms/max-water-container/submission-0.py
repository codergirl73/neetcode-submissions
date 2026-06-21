class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left = 0
        right = len(heights)-1

        max_water = 0


        while left < right:

            width = right - left

            min_height = min(heights[left], heights[right])

            current_water = width * min_height 

            max_water = max(current_water, max_water)

            if heights[left]<heights[right]:

                left+=1
            else:
                right-=1

        return max_water
        
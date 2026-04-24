class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        l, r = 0, n - 1
        maxWater = 0

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            maxWater = max(maxWater, area)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return maxWater
class Solution(object):
    def maxArea(self, height):
        area = float("-Inf")
        pt1 = 0
        pt2 = len(height) - 1
        while pt1 != pt2:
            currArea = min(height[pt1], height[pt2]) * (pt2 - pt1)
            if currArea > area:
                area = currArea
            else:
                if height[pt1] < height[pt2]:
                    pt1 += 1
                else:
                    pt2 -= 1
        return area
        
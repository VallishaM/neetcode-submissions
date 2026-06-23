class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        max_area = 0
        while start < end:
            hstart = heights[start]
            hend = heights[end]
            area = (end - start) * min(hstart, hend)
            if area > max_area:
                max_area = area
            if hstart < hend:
                start += 1
            elif hstart > hend:
                end -= 1
            else:
                start += 1
                end -= 1
        return max_area
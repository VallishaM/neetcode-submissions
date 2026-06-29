class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        rightMax = -1
        leftMax = -1
        area = 0
        
        while l < r:
            rightMax = max(rightMax, height[r])
            leftMax = max(leftMax, height[l])

            if rightMax <=  leftMax:
                area += rightMax - height[r]
                r -= 1
            else:
                area += leftMax - height[l]
                l += 1
        
        return area
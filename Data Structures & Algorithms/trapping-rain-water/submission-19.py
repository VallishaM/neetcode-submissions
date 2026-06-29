class Solution:
    def trap(self, height: List[int]) -> int:
        prev_max = -1

        n = len(height)
        right_limit= [-1 for _ in range(n)]
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                prev_max = height[i]
                right_limit[i] = -2
            else:
                
                if height[i] >= prev_max:
                    right_limit[i] = -1
                    prev_max = height[i]
                else:
                    right_limit[i] = prev_max

        left_limit= [-1 for _ in range(n)]
        prev_max = -1

        for i in range(0, n, 1):
            if i == 0:
                prev_max = height[i]
                left_limit[i] = -2
            else:
                
                if height[i] >= prev_max:
                    left_limit[i] = -1

                    prev_max = height[i]
                else:
                    left_limit[i] = prev_max

        # print(height)
        # print(left_limit)
        # print(right_limit)
        total = 0
        for i in range(1, n-1, 1):
            area = min(left_limit[i], right_limit[i]) - height[i]
            if area > 0:
                total += area
        return total

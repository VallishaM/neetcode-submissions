class Solution:
    def trap(self, height: List[int]) -> int:
        prev_max = -1
        min_in_window = -1
        min_ind = -1
        n = len(height)
        right_limit= [-1 for _ in range(n)]
        for i in range(n - 1, -1, -1):
            if i == n - 1:
                prev_max = height[i]
                right_limit[i] = -2
            else:
                
                if height[i] >= prev_max:
                    if min_ind > 0:
                        right_limit[i] = right_limit[min_ind]
                    else:
                        right_limit[i] = -1

                    min_in_window = -1
                    min_ind = -1
                    prev_max = height[i]
                else:
                    right_limit[i] = prev_max
                    if min_in_window > height[i] or min_in_window < 0:
                        min_in_window = height[i]
                        min_ind = i

        left_limit= [-1 for _ in range(n)]
        prev_max = -1
        min_in_window = -1
        min_ind = -1
        for i in range(0, n, 1):
            if i == 0:
                prev_max = height[i]
                left_limit[i] = -2
            else:
                
                if height[i] >= prev_max:
                    if min_ind > 0:
                        left_limit[i] = left_limit[min_ind]
                    else:
                        left_limit[i] = -1

                    min_in_window = -1
                    min_ind = -1
                    prev_max = height[i]
                else:
                    left_limit[i] = prev_max
                    if min_in_window > height[i] or min_in_window < 0:
                        min_in_window = height[i]
                        min_ind = i
        # print(height)
        # print(left_limit)
        # print(right_limit)
        total = 0
        for i in range(1, n-1, 1):
            area = min(left_limit[i], right_limit[i]) - height[i]
            if right_limit[i] > 0 and left_limit[i] > 0 and area > 0:
                total += area
        return total

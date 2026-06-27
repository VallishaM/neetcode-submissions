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
        start = 0
        end = 1
        total = 0
        running_sum = 0
        #print(right_limit)
        while end < n and start < end:
            
            if right_limit[start] == -1:
                start += 1
                area = (end - start - 1) * min(height[end], height[start]) - running_sum
                
                if area > 0:
                    total += area
                running_sum = 0
                if end == start:
                    end += 1
            else:
                he = height[end]
                hs = height[start]
                
                if he >= hs or end == n-1:
                    area = (end - start - 1) * min(he, hs) - running_sum
                    
                    total += area
                    running_sum = 0
                    start = end
                    end += 1
                else:
                    running_sum += he
                    end += 1
        return total

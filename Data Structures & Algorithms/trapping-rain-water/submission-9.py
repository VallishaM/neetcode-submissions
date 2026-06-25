class Solution:
    def trap(self, height: List[int]) -> int:
        running_sum = 0
        start = 0
        end = start + 1
        max_area = 0
        max_in_window = 0
        max_in_window_pos = -1
        max_in_window_sum = 0
        while end < len(height):
            he = height[end]
            hs = height[start]
            if he >= hs:
                area = (end - start - 1) * min(he, hs) - running_sum
                
                max_area += area
                running_sum = 0
                start = end
                max_in_window = 0
                max_in_window_pos = -1
                max_in_window_sum = 0
                
            else:
                running_sum += he
                if he > max_in_window:
                    max_in_window = he
                    max_in_window_pos = end
                    max_in_window_sum = running_sum
                if end == len(height) - 1:
                    if max_in_window > he:
                        start = start + 1
                        end = max(max_in_window_pos, start + 1)

                        running_sum = max_in_window_sum if start + 1 < max_in_window_pos else height[end]
                        max_in_window = max_in_window if start + 1 < max_in_window_pos else height[end]
                        
                    else:
                        
                        area = (end - start - 1) * he - (running_sum - he)
                        
                        max_area += area

            end += 1
        return max_area
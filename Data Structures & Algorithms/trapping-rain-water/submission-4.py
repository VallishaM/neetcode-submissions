class Solution:
    def trap(self, height: List[int]) -> int:
        running_sum = 0
        start = 0
        end = start + 1
        max_area = 0
        max_in_window = 0
        while end < len(height):
            he = height[end]
            hs = height[start]
            if he >= hs:
                area = (end - start - 1) * min(he, hs) - running_sum
                print(start, end, hs, he, area, max_area)
                max_area += area
                running_sum = 0
                start = end
                max_in_window = 0
                
            else:
                running_sum += he
                if he > max_in_window:
                    max_in_window = he
                if end == len(height) - 1:
                    if max_in_window > he:
                        start = start + 1
                        end = start
                        running_sum = 0
                        max_in_window = 0
                    else:
                        
                        area = (end - start - 1) * he - (running_sum - he)
                        #print(start, end, hs, he, running_sum, area, max_area, max_in_window)
                        max_area += area
            end += 1
        return max_area
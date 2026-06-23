class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        print(nums)
        l = len(nums)
        base = 0
        while base <= l-3:
            target = -1 * nums[base]
            start = base + 1
            end = l - 1
            found = False
            
            while start < end:
                if nums[start] + nums[end] == target:
                    found = True
                    res.append([nums[base], nums[start], nums[end]])
                    
                    new_start = start + 1
                    while new_start <= end and nums[new_start] == nums[start]:
                        new_start += 1
                    start = new_start

                    new_end = end - 1
                    while new_end >= start and nums[new_end] == nums[end]:
                        new_end -= 1
                    end = new_end
                elif nums[start] + nums[end] < target:
                    new_start = start + 1
                    start = new_start
                else:
                    new_end = end - 1

                    end = new_end
            new_base = base + 1
            
            while found and new_base <= l-2 and nums[new_base] == nums[base]:
                
                new_base += 1
            base = new_base
        return res
            
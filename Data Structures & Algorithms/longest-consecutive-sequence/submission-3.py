class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mem = {}
        max_len = 0
        for n in nums:
            mem[n] =  [False, -1]
        
        for n in mem:
            next_number = n
            if not mem[n][0]:
                next_number = n + 1
                while (next_number in mem) and (not mem[next_number][0]):
                    mem[next_number][0] = True
                    next_number += 1
                if next_number in mem and mem[next_number]:
                    next_number = mem[next_number][1]
                else:
                    next_number -= 1
            mem[n][1] = next_number
            mem[n][0] = True
            if max_len < next_number - n + 1:
                max_len = next_number - n + 1
        
        return max_len
                



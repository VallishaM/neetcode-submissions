class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mem = {}
        max_len = 0
        for n in nums:
            mem[n] =  False
        ans_mem = {}
        for n in mem:
            next_number = n
            if not mem[n]:
                next_number = n + 1
                while (next_number in mem) and (not mem[next_number]):
                    mem[next_number] = True
                    next_number += 1
                if next_number in mem and mem[next_number]:
                    next_number = ans_mem[next_number]
            ans_mem[n] = next_number
            mem[n] = True
            if max_len < next_number - n:
                max_len = next_number - n

        return max_len
                



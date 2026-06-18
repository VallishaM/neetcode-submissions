class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        for i, n in enumerate(nums):
            if (target - n) in mem:
                return [mem[target - n], i]
            mem[n] = i
        return [-1, -1]
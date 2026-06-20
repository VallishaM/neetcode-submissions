class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1 for _ in nums]
        l = len(nums)
        

        for i in range(1, l):
            prefix.append(prefix[i-1] * nums[i-1])

        for i in range(l-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        return [prefix[i] * suffix[i] for i in range(0, l)]

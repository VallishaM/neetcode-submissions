class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        max_len = 0
        for i in s:
            if i - 1 not in s:
                curr_element = i
                length = 1
                while curr_element + 1 in s:
                    curr_element += 1
                    length += 1
                if length > max_len:
                    max_len = length
        return max_len
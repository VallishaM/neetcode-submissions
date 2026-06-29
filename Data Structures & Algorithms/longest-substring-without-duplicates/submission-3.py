class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return n
        l = 0
        r = 1
        maxLength = 1
        window = {}
        window[s[l]] = l
        while r < n:

            if s[r] in window and window[s[r]] >= l:
                l = window[s[r]] + 1
                window[s[r]] = r
                r += 1
            else:
                window[s[r]] = r
                
                maxLength = max(maxLength, r - l + 1)
                r += 1

        return maxLength
class Solution:
    def isValid(self, freq_w, freq_t):
        for c in freq_t:
            if freq_w.get(c, 0) < freq_t[c]:
                return False
        return True
    def minWindow(self, s: str, t: str) -> str:
        freq_s = {}
        freq_t = {}
        len_s = len(s)
        len_t = len(t)

        if len_t > len_s:
            return ""

        for c in t:
            freq_t[c] = freq_t.get(c, 0)+1
        
        freq_w = {}
        l = 0
        r=0

        minLength = -1
        minStr = ""

        while r < len_s and l <= r:
            r_old=r
            old_l=l
            
            freq_w[s[r]] = freq_w.get(s[r], 0) + 1

            old_freq_w = freq_w.copy()

            if r-l+1>=len_t and self.isValid(freq_w, freq_t):
                while freq_w[s[l]] > freq_t.get(s[l], 0) and l<r :
                    freq_w[s[l]] -= 1
                    l += 1
                
                while freq_w[s[r]] > freq_t.get(s[r], 0) and l<r:
                    freq_w[s[r]] -= 1
                    r -= 1

                if (minLength > r-l+1 or minLength == -1):
                    minStr = s[l:r+1]
                    minLength = r - l + 1
                l=l+1
                while old_l<l:
                    old_freq_w[s[old_l]] -= 1
                    old_l += 1
                freq_w=old_freq_w.copy()
                r=r_old+1
                
            else:
                r=r+1


        return minStr

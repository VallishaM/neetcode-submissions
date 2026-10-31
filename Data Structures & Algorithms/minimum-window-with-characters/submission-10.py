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

        uct = len(freq_t.keys())
        
        freq_w = {}
        l = 0
        r=0

        minLength = -1
        minStr = ""
        mc=0

        ms={}

        while r < len_s and l <= r:
            r_old=r
            
            freq_w[s[r]] = freq_w.get(s[r], 0) + 1
            if s[r] in freq_t and freq_w.get(s[r], 0) == freq_t[s[r]]:
                mc+=1
            if r-l+1>=len_t and uct==mc:
 
                while freq_w[s[l]] > freq_t.get(s[l], 0) and l<r :
                    freq_w[s[l]] -= 1
                    if s[l] in freq_t and freq_w[s[l]] < freq_t[s[l]]:
                        mc -= 1
                    l += 1
                
                if (minLength > r-l+1 or minLength == -1):
                    minStr = s[l:r+1]
                    minLength = r - l + 1
                
                freq_w[s[l]] -= 1
                if s[l] in freq_t and freq_w[s[l]] < freq_t[s[l]]:
                    mc -= 1
                l=l+1
                r=r_old+1
                
            else:
                r=r+1


        return minStr

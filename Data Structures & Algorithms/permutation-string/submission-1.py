class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ls1 = len(s1)
        ls2 = len(s2)

        ord_a = ord('a')
        
        if ls2 < ls1:
            return False
        freq_s1 = [0 for _ in range(26)]
        
        for c in s1:
            freq_s1[ord(c) - ord_a] += 1

        start = 0
        end = ls1 - 1
        freq_running = [0 for _ in range(26)]

        

        for start in range(0, ls2-ls1+1):
            
            if start == 0:
                for i in range(start, start+ls1):
                    freq_running[ord(s2[i])-ord_a] += 1
            else:
                freq_running[ord(s2[start - 1])-ord_a] -= 1
                freq_running[ord(s2[start+ls1-1])-ord_a] += 1
            if freq_running == freq_s1:
                return True
        return False
                    


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f1 = [0] * 26
        f2 = [0] * 26

        l1 = len(s)
        l2 = len(t)

        if l1 != l2:
            return False
        
        ord_a = ord('a')
        
        for i in range(0, l1):
            f1[ord(s[i]) - ord_a] += 1
            f2[ord(t[i]) - ord_a] += 1
        
        for i in range(0, 26):
            if f1[i] != f2[i]:
                return False
        
        return True
        
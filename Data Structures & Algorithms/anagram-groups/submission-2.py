class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mem={}
        ord_a = ord('a')
        for s in strs:
            fn=[0]*26
            for c in s:
                fn[ord(c) - ord_a] += 1

            key = tuple(fn)
            mem.setdefault(key, []).append(s)
        return list(mem.values())
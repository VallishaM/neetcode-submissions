class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mem={}
        ord_a = ord('a')
        for s in strs:
            fn=[0]*26
            for c in s:
                fn[ord(c) - ord_a] += 1
            if tuple(fn) in mem:
                mem[tuple(fn)].append(s)
            else:
                mem[tuple(fn)] = [s]
        return list(mem.values())
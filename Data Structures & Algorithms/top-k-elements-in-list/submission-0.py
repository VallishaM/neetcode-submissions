class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
        
        inv_f = {}
        for f in freq:
            if freq[f] in inv_f:
                inv_f[freq[f]].append(f)
            else:
                inv_f[freq[f]] = [f]

        fs = list(inv_f.keys())
        fs.sort(reverse=True)
        res = []
        c = 0

        while len(res) < k and c < len(fs):
            j = 0
            while j < len(inv_f[fs[c]]) and len(res) < k:
                res.append(inv_f[fs[c]][j])
                j+=1
            c+=1
        return res
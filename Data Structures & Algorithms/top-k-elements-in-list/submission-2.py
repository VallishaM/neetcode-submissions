class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        inv_f = {}
        for f in freq:
            inv_f.setdefault(freq[f], []).append(f)

        fs = list(inv_f.keys())
        
        buckets = [0]*1000

        for f in fs:
            buckets[f] = 1
        
        fs_sorted = []

        for i in range(len(buckets) - 1, -1, -1): 
            if buckets[i] == 1:
                fs_sorted.append(i)

        res = []
        c = 0

        while len(res) < k and c < len(fs_sorted):
            j = 0
            while j < len(inv_f[fs_sorted[c]]) and len(res) < k:
                res.append(inv_f[fs_sorted[c]][j])
                j+=1
            c+=1
        return res
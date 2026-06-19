class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]
        maxBucket = 0
        for num, count in freq.items():
            buckets[count].append(num)
            if count > maxBucket:
                maxBucket = count

        res = []
        count = 0

        for i in range(maxBucket, 0, -1):
            for n in buckets[i]:
                count += 1
                res.append(n)
                if count == k:
                    return res
        
        return res
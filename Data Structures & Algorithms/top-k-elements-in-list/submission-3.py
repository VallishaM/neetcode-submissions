class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)

        res = []
        count = 0

        for i in range(len(nums), 0, -1):
            for n in buckets[i]:
                count += 1
                res.append(n)
                if count == k:
                    return res
        
        return res
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        p=1
        nzp=1
        mem={}
        for n in nums:
            p *= n
            if n==0:
                zero_count+=1
            else:
                nzp *= n
            mem[n] = mem.get(n, 0) + 1

        
        
        if zero_count>1:
            nzp=0
            p=0
            return [0 for _ in nums]
        if zero_count==1:
            res=[]
            for n in nums:
                if n==0:
                    res.append(nzp)
                else:
                    res.append(0)
            return res
        
        res = []
        for n in nums:
            ans = 1
            for k in mem:
                p = mem[k]
                if k == n:
                    p -= 1
                ans *= k ** p
            res.append(ans)
        return res
        

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = 0
        p=1
        for n in nums:
            p *= n
            if n==0:
                zero_count+=1

        nzp=1
        
        if zero_count>1:
            nzp=0
            p=0
            return [0 for _ in nums]
        if zero_count==1:
            for n in nums:
                if n!=0:
                    nzp *= n
            res=[]
            for n in nums:
                if n==0:
                    res.append(nzp)
                else:
                    res.append(0)
            return res
        return [int(p/n) for n in nums]
        

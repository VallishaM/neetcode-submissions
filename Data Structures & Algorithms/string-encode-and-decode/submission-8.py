class Solution:

    def encode(self, strs: List[str]) -> str:
        res=[]
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)      
        return ''.join(res)
            

    def decode(self, s: str) -> List[str]:
        res = []
        running_len = []
        i = 0
        while i < len(s):
            if s[i] == '#':
                length = int(''.join(running_len))
                next_string = s[i+1:i+1+length]
                running_len = []
                i = i+1+length
                res.append(next_string)
            else:
                running_len.append(s[i])
                i+=1
        return res
        
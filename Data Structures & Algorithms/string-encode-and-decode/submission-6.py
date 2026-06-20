class Solution:

    def encode(self, strs: List[str]) -> str:
        res=''
        for s in strs:
            res = res + str(len(s)) + '#' + s
        return res
            

    def decode(self, s: str) -> List[str]:
        res = []
        running_str = ''
        i = 0
        while i < len(s):
            if s[i] == '#':
                length = int(running_str)
                next_string = s[i+1:i+1+length]
                running_str = ''
                i = i+1+length
                res.append(next_string)
            else:
                running_str += s[i]
                i+=1
        return res
        
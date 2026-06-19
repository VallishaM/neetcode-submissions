class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs)==0:
            return chr(257)
        res = chr(0).join(strs)
        print(res)
        return res
            

    def decode(self, s: str) -> List[str]:
        if s==chr(257):
            return []
        return s.split(chr(0))
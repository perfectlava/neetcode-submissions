class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""
        
        if len(strs) == 0:
            return "空"
        
        for i in range(len(strs)-1):
            out += strs[i] + "分"

        out += strs[-1]
        return out
    
    def decode(self, s: str) -> List[str]:
        if s != "空":
            return s.split("分")
        return []

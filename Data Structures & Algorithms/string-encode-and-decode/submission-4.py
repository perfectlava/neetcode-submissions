class Solution:

    def encode(self, strs: List[str]) -> str:
        
        if len(strs) == 0:
            return ""

        out = ""

        for s in strs:
            out += chr(len(s)) + s

        return out
    
    def decode(self, s: str) -> List[str]:
        
        if s == "":
            return []
        elif len(s) == 1:
             return [""]
        
        
        i = 0
        out = []
        while i < len(s):
            out.append(s[i + 1 : 1 + i + ord(s[i])])
            i += ord(s[i]) + 1
        return out

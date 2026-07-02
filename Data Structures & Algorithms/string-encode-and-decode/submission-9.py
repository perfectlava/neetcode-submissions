class Solution:

    def encode(self, strs: List[str]) -> str:
        
        if len(strs) == 0:
            return ""
        
        out = "" 
        for s in strs:
            out += f"{len(s)}-{s}"
        return out

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        i = 0
        out = []

        while i < len(s):
            length = ""

            while i < len(s) and s[i] != "-":
                length += s[i]
                i += 1

            if int(length) == 0:
                out.append("")
            else:
                out.append(s[i + 1 : i + int(length)+1])    # 0-

            i += int(length) + 1
        
        return out

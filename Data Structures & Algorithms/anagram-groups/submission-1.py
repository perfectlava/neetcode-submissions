class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        seen = defaultdict(list)

        for s in strs:
            sign = [0] * 26
            
            for c in s.lower():
                sign[ord(c) - ord('a')] += 1
            
            seen[str(sign)].append(s)

        return list(seen.values())
        
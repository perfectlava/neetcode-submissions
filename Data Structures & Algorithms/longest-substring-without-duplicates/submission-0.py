class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        curr = set()
        maxL = 0
        
        for r in range(len(s)):
            
            while s[r] in curr:
                curr.remove(s[l])
                l += 1
            
            if s[r] not in curr:
                curr.add(s[r])
            
            maxL = max(maxL, len(curr))
        
        return maxL
            
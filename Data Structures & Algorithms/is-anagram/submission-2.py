class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char = defaultdict(int)
        if len(s) != len(t): 
            return False
            
        for sChar in s:
            char[sChar] += 1
        
        for tChar in t:
            char[tChar] -= 1
            if char[tChar] < 0:
                return False
        return True
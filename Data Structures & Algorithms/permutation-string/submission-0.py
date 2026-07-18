class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        s1_m = defaultdict(int)
        s2_m = defaultdict(int)

        for char in s1:
            s1_m[char] += 1

        for r in range(len(s2)):
            s2_m[s2[r]] += 1
        
            if r - l == len(s1) - 1:
                if s2_m == s1_m:
                    return True
                else:
                    s2_m[s2[l]] -= 1
                    if s2_m[s2[l]] == 0:
                        del s2_m[s2[l]]
                    l += 1
        
        return False


            


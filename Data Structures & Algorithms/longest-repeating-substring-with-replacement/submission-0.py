class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        data = defaultdict(int)
        maxL = 0
        maxF = ["", 0]
        
        for r, char in enumerate(s):
            data[char] += 1
            if data[char] > maxF[1]:
                maxF = [char, data[char]]
            if (r - l - maxF[1] + 1) > k:
                print(f"cut {s[l]}")
                if s[l] == maxF[0]:
                    maxF[1] -= 1

                data[s[l]] -= 1

                l += 1

            print(f"{r - l}")
            
            maxL = max(maxL, r - l + 1)
            
        return maxL
                

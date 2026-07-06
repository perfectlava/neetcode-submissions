class Solution:
    def isPalindrome(self, s: str) -> bool:
        numbers = {"0","1","2","3","4","5","6","7","8","9"}
        x = 0
        y = len(s) - 1
        while x < y:
            while x < y and s[x].lower() == s[x].upper() and not s[x] in numbers:
                x += 1
            
            while x < y and s[y].lower() == s[y].upper() and not s[y] in numbers:
                y -= 1

            if s[x].lower() != s[y].lower():
                return False
            x += 1
            y -= 1 

        return True

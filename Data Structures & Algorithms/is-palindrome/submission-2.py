class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        numbers = {"0","1","2","3","4","5","6","7","8","9"}

        for char in s:
            if char.lower() != char.upper() or char in numbers:
                clean += char.lower()
        
        for i in range(len(clean) // 2):
            if clean[i] != clean[len(clean) - i - 1]:
                return False
        
        return True
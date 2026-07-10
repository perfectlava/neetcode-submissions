class Solution:
    def isValid(self, s: str) -> bool:
        open_close = {"}" : "{", "]" : "[", ")" : "("}
        open_stack = []
        for c in s:
            if c in open_close:
                if len(open_stack) == 0 or open_stack.pop() != open_close[c]:
                    return False
            else:
                open_stack.append(c)
        return len(open_stack) == 0


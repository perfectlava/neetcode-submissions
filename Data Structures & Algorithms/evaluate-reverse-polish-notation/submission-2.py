class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        for t in tokens:
            if t == "+":
                n2 = nums.pop()
                n1 = nums.pop()
                nums.append(n1 + n2)
            elif t == "-":
                n2 = nums.pop()
                n1 = nums.pop()
                nums.append(n1 - n2)
            elif t == "*":
                n2 = nums.pop()
                n1 = nums.pop()
                nums.append(n1 * n2)
            elif t == "/":
                n2 = nums.pop()
                n1 = nums.pop()
                nums.append(int((n1 + 0.5) / n2))
            else:
                nums.append(int(t))
            print(nums)
        return nums[-1]
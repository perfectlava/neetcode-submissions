class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #brute force :
        out = []
        for index, num in enumerate(nums):
            product = 1
            for i, n in enumerate(nums):
                if i != index:
                    product *= n
            out.append(product)
        return out
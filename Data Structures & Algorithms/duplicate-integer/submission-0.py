class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        found = {}
        for num in nums:
            if found.get(str(num)):
                return True
            found[str(num)] = True
        return False
        
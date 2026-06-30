class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        saved = {}
        for index, num in enumerate(nums):
            if saved.get(target - num) != None:
                return [saved.get(target - num), index]
            saved[num] = index
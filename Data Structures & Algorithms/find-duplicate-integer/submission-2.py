class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = 0
        

        while fast == 0 or not fast == slow:
            fast = nums[fast]
            fast = nums[fast]

            slow = nums[slow]

        other = 0
        
        while not other == slow:
            other = nums[other]
            slow  = nums[slow]

        return slow

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            m = nums[mid] 
            
            if m == target:
                return mid

            if m < nums[r]: # m--> 4, 5, 7 <-- r
                if target > m:
                    if target > nums[r]:
                        r = mid - 1
                    else:
                        l = mid + 1
                else:
                    r = mid - 1
            else: # m --> 8, 10, 4, 6 <-- r
                if target > m:
                    l = mid + 1
                else:
                    if target > nums[r]:
                        r = mid - 1
                    else:
                        l = mid + 1


        
        
        return -1 
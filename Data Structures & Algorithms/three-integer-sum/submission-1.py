class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out_set = set()

        print(nums)

        for i, n in enumerate(nums):
            j = len(nums) - 1
            k = 0
            target_sum = -n
            while j > k:
                curr_sum = nums[j] + nums[k]
                if j == i or curr_sum > target_sum:
                    j -= 1
                elif k == i or curr_sum < target_sum:
                    k += 1
                else:
                    new_item = sorted([n, nums[j], nums[k]])
                    out_set.add(tuple(new_item))
                    k += 1
                    j -= 1
        return [list(t) for t in out_set]

            

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #1  2  8 48
        #48 24 12 8
        pref = [nums[0]]
        post = [nums[-1]]
        
        for i in range(1, len(nums)):
            pref.append(pref[i-1] * nums[i]) 
            post.append(post[i-1] * nums[len(nums)-i-1])
            #6, 24, 48, 48
        post.reverse()
        pref.append(1)
        pref.insert(0, 1)
        post.append(1)
        post.insert(0, 1)

        print(post)
        print(pref)

        out = []
        for i in range(len(post)-2):
            out.append(pref[i]*post[i+2])
        return out

        
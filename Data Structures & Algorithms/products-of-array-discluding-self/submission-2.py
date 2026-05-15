class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pref = [0] * n
        suff = [0] * n

        for i in range(n):
            if i == 0:
                pref[i] = 1
                suff[-(i+1)] = 1
            else:
                pref[i] = pref[i-1] * nums[i-1]
                suff[-(i+1)] = suff[-i] * nums[-i]

        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res
        
            


        
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        r = len(nums) - 1
        i = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                return res
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while r > l:
                total = nums[i] + nums[r] + nums[l]

                if total == 0:
                    res.append([nums[i],nums[r],nums[l]])
                    r-=1
                    l+=1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1    
                elif total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
            
        return res

        
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while r > l + 1:
            if nums[l] < nums[r]:
                return min(nums[l],nums[r])
            
            m = l + (r-l)//2
            print(l,m,r)

            if nums[m] > nums[l]:
                l = m + 1
            elif nums[m] < nums[l]:
                r = m
        return min(nums[l],nums[r])
        
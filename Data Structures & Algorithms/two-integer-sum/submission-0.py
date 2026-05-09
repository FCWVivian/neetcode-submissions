class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pointer_a, pointer_b = 0, 0
        for pointer_a in range(len(nums)):
            temp = target - nums[pointer_a]
            pointer_b = pointer_a + 1
            while pointer_b < len(nums):
                if nums[pointer_b] == temp:
                    return [pointer_a, pointer_b]
                else:
                    pointer_b +=1
        return False
        
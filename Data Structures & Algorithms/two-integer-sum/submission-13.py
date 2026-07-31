class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {}

        for i, num in enumerate(nums):
            if num not in hash_map:
                hash_map[target - num] = i
            else:
                return [hash_map[num], i]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            hash_map[target - nums[i]] = i
        for j, num in enumerate(nums):
            if num in hash_map.keys() and hash_map[num] != j:
                return [j, hash_map[num]]
        return False
        
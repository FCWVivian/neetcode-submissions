class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx_1, idx_2 = 0, len(numbers) - 1
        while idx_2 > idx_1:
            if (numbers[idx_1] + numbers[idx_2]) == target:
                return [idx_1 + 1, idx_2 + 1]
            elif (numbers[idx_1] + numbers[idx_2]) > target:
                idx_2 -= 1
            elif (numbers[idx_1] + numbers[idx_2]) < target:
                idx_1 += 1
        return [idx_1 + 1, idx_2 + 1]
                


        
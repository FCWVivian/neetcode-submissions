class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            print("num:",num, ", length:",longest)
            if num - 1 not in numSet:
                length = 1
                while (num + length) in numSet:
                    print("num:",num, ", length:",length)
                    length += 1
                longest = max(length, longest)
        return longest

        
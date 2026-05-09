class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}
        for i in nums:
            print(dictionary)
            if i not in dictionary.keys():
                dictionary[i] = 1
            else:
                return True

        return False
        
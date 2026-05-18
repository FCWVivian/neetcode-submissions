class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        count = []
        i = 0
        while i < len(s):
            print(count)
            if s[i] not in count:
                count.append(s[i])
                i += 1
            else:
                longest = max(len(count), longest)
                for j in range(len(count)):
                    if count[j] == s[i]:
                        count = count[j+1:]
                        break
                

        return max(len(count), longest)

        
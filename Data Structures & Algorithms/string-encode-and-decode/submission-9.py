class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + "#" + s

        return res


    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        length = 0
        while i < len(s):
            if s[i] == "#":
                ans.append(s[i+1: i+1+length])
                i += (length + 1)
                length = 0
            else:
                length = length * 10 + int(s[i])
                i += 1
        return ans

            

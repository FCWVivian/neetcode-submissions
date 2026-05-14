class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res = res + str(len(s)) + "#" + s
        print(res)
        return res


    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        print(s)

        anchor = 0
        while i < len(s):
            print(i)
            if s[i] == "#":
                j = i -1
                length = 0
                decimal = 1
                while j >= anchor and s[j].isdigit():
                    length = int(s[j])*decimal +length
                    j = j - 1
                    decimal = decimal*10 

                temp = s[i+1: i+1+length]
                ans.append(temp)
                
                i += (length + 1)
                anchor = i
            else:
                i += 1
        return ans

            

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count1 = {}
        count2 = {}
        l, r = 0, len(s1) - 1
        if len(s2)<len(s1):
            return False

        for i in range(len(s1)):
            count1[s1[i]] = count1.get(s1[i], 0) + 1
            count2[s2[i]] = count2.get(s2[i], 0) + 1



        while r < (len(s2)-1):
            print('r:',r, ' l:', l)
            print(count1)
            print(count2)

            if count1 == count2:
                return True
            else:
                if count2[s2[l]] == 1:
                    del count2[s2[l]]
                else:
                    count2[s2[l]] -= 1
                
                l += 1
                r += 1
                count2[s2[r]] = count2.get(s2[r], 0) + 1
        return count1 == count2





        

        
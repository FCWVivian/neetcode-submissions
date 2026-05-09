class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        dict_t = {}
        if len(s)!= len(t):
            return False
        for i in range(len(s)):
            if s[i] not in dict_s.keys():
                dict_s[s[i]] = 1
            else: 
                dict_s[s[i]] += 1
            if t[i] not in dict_t.keys():
                dict_t[t[i]] = 1
            else: 
                dict_t[t[i]] += 1
        return dict_s == dict_t
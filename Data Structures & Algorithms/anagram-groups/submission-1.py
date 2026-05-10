class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for s in strs:
            temp = "".join(sorted(s))
            if temp not in hash_map.keys():
                hash_map[temp] = [s]
            else:
                hash_map[temp].append(s)
        ans = []
        for key in hash_map.keys():
            ans.append(hash_map[key])
        return ans
        
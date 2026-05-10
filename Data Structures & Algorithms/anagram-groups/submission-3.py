class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}

        for s in strs:
            temp = "".join(sorted(s))
            if temp not in hash_map.keys():
                hash_map[temp] = [s]
            else:
                hash_map[temp].append(s)
        return list(hash_map.values())
        
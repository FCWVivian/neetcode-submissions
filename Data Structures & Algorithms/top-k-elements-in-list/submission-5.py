class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        for i in nums:
            hash_map[i] = 1 + hash_map.get(i, 0)
        arr = []
        for num, count in hash_map.items():
            arr.append([count, num])
        arr.sort()
        ans = []
        print(arr)
        for i in range(k):
            print(i+1)
            ans.append(arr[-(i+1)][1])
        return ans


        
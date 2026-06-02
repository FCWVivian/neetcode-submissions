class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        u, l = max(piles), 1
        res = u
        

        while u >= l:
            total_t = 0
            k = l + (u - l)//2
            for p in piles:
                total_t += math.ceil(float(p)/k)
            if total_t <= h:
                res = k
                u = k - 1
            else:
                l = k + 1
        return res
        
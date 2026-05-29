class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        count = 0
        max_time = 0

        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        for p,s in pair:
            temp_time = (target - p)/s
            if temp_time > max_time:
                count += 1
                max_time = temp_time
        return count

        





        
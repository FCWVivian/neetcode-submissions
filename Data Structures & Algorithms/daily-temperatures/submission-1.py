class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                temp_t, temp_i = stack.pop()
                res[temp_i] = i - temp_i
            stack.append([t,i])
        return res

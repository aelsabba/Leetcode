### inspired by cracking FAANG

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        days = [0] * len(temperatures)
        stack = []

        for cur_day, cur_temp in enumerate(temperatures):
            while stack and cur_temp > stack[-1][1]:
                prev_day, prev_temp = stack.pop()

                days[prev_day] = cur_day - prev_day

            stack.append((cur_day, cur_temp))

        return days
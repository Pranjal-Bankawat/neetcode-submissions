class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            
            while (len(stack) and temperatures[stack[-1]] < temperatures[i]):
                colder_temp_day = stack.pop()
                res[colder_temp_day] = i - colder_temp_day
            stack.append(i)

        return res
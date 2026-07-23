class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        first = 0
        last = len(numbers) - 1
        while first < last:
            diff = target - numbers[first]
            if numbers[last] > diff:
                last -= 1
                continue
            if numbers[last] < diff:
                first += 1
                continue
            if numbers[last] == diff:
                res.append(first+1)
                res.append(last+1)
                break
        return res
            
            
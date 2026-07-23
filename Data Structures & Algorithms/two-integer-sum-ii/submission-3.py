class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            if numbers[l] == target - numbers[r]:
                return [l+1, r+1]
            elif numbers[l] < target - numbers[r]:
                l += 1
            else:
                r -= 1
        return [0,0]

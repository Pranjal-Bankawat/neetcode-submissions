class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        nums.sort()

        def backtrack(path, i):
            if i == len(nums) and path not in res:
                res.append(path[:])
                return
            if i >= len(nums):
                return
            path.append(nums[i])
            backtrack(path, i+1)
            path.pop()
            backtrack(path, i+1)
        backtrack([], 0)
        return res

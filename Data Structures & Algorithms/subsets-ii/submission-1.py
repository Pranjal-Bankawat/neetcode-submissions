class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(path, i):
            res.append(path[:])
            
            for idx in range(i, len(nums)):
                if idx > i and nums[idx] == nums[idx-1]:
                    continue
                path.append(nums[idx])
                backtrack(path, idx+1)
                path.pop()
        backtrack([], 0)
        return res

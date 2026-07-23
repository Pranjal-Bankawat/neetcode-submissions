class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, path, t):
            if t == target and path not in res:
                res.append(path[:])
                return
            if t > target or i >= len(nums):
                return
            path.append(nums[i])
            dfs(i, path, t+nums[i])
            path.pop()
            dfs(i+1, path, t)
        dfs(0, [], 0)
        return res
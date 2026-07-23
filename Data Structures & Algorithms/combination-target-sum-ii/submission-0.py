class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, path, total):
            if total == target and path not in res:
                res.append(path[:])
                return
            if total > target or i >= len(candidates):
                return
            path.append(candidates[i])
            dfs(i+1, path, total+candidates[i])
            path.pop()
            dfs(i+1, path, total)
        dfs(0, [], 0)
        return res

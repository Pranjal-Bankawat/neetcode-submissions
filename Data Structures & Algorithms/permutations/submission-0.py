class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack(nums, 0)
        return self.res
    
    def backtrack(self, path: List[int], i: int):
        if i == len(path):
            self.res.append(path[:])
            return
        for idx in range(i, len(path)):
            path[i], path[idx] = path[idx], path[i]
            self.backtrack(path, i + 1)
            path[i], path[idx] = path[idx], path[i]
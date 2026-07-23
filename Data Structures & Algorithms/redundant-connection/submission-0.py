class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        par = [i for i in range(n + 1)]
        size = [1] * (n + 1)

        def find(x):
            if par[x] != x:
                par[x] = find(par[x])  # full path compression
            return par[x]

        def union(x, y):
            px, py = find(x), find(y)

            if px == py:
                return [x, y]

            if size[px] > size[py]:
                par[py] = px
                size[px] += size[py]
            else:
                par[px] = py
                size[py] += size[px]

            return None

        for x, y in edges:
            res = union(x, y)
            if res:
                return res
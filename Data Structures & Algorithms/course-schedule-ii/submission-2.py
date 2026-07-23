class Solution:
    def findOrder(self, numCourses, prerequisites):
        preMap = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting = set()
        visited = set()
        order = []

        def dfs(crs):
            if crs in visiting:   # cycle
                return False
            if crs in visited:    # already processed
                return True

            visiting.add(crs)

            for pre in preMap[crs]:
                if not dfs(pre):
                    return False

            visiting.remove(crs)
            visited.add(crs)
            order.append(crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []

        return order
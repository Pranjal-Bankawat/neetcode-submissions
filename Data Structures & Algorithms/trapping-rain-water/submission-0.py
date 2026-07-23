class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        n = len(height)
        pref_max = [0] * n
        suff_max = [0] * n

        pref_max[0] = height[0]
        for i in range(1,n):
            pref_max[i] = max(pref_max[i-1], height[i])

        suff_max[n-1] = height[n-1]
        for i in range(n-2,-1,-1):
            suff_max[i] = max(suff_max[i+1], height[i])

        for i in range(n):
            total += min(pref_max[i], suff_max[i]) - height[i]
        
        return total
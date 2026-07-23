class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = float('infinity')

        while l <= r:
            m = ( l + r ) // 2

            if nums[m] <= nums[r] and nums[m] <= nums[l]:
                res = min(res, nums[m])
                r = m - 1
            elif nums[m] >= nums[r]:
                l = m + 1
            else:
                r = m - 1
        return res
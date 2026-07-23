class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_arr = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            product_arr[i] = prefix
            prefix *= nums[i]

        suffix = 1

        for j in range(len(nums)-1, -1, -1):
            product_arr[j] *= suffix
            suffix *= nums[j]

        return product_arr

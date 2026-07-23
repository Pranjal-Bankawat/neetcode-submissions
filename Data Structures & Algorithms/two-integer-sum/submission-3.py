class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        key_value = {}

        for i in range(len(nums)):
            x = target - nums[i]
            if x in key_value.keys():
                return [key_value[x], i]
            else:
                key_value[nums[i]] = i
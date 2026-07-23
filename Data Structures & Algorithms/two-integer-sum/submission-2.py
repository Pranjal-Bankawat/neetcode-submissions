class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        key_value = {}
        coords = []
        for i in range(len(nums)):
            x = target - nums[i]
            if x in key_value:
                coords.append(key_value[x])
                coords.append(i)
            else:
                key_value[nums[i]] = i
        
        return coords
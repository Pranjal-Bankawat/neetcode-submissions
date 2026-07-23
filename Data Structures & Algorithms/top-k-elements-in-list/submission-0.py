class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        for num in nums:
            res[num] += 1
        buckets = [[] for _ in range(len(nums))]
        for key in res:
            buckets[res[key]-1].append(key)
        sorted_arr = []
        for bucket in buckets:
            sorted_arr.extend(bucket)
        return sorted_arr[-k:]
        
        

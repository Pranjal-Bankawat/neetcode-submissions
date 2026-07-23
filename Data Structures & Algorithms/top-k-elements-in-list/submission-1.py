class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = defaultdict(int)
        for num in nums:
            res[num] += 1
        buckets = [[] for _ in range(len(nums)+1)]
        for key,val in res.items():
            buckets[val].append(key)
        x = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                x.append(num)
                if len(x) == k:
                    return x
        
        

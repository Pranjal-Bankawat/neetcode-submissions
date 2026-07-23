class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            print(f'First: {first}')
            second = heapq.heappop(stones)
            print(f'Second: {second}')
            if second > first:
                heapq.heappush(stones, first-second)
        stones.append(0)
        return abs(stones[0])
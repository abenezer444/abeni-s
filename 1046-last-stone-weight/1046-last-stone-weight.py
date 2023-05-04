class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-i for i in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            temp=heapq.heappop(stones)-heapq.heappop(stones)
            heapq.heappush(stones,temp)
        return -stones[0]
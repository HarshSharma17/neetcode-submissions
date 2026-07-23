from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        if k == len(nums):
            return nums

        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        heap = []
        for num in count:
            heapq.heappush(heap,(count[num], num))

            if len(heap) > k:
                heapq.heappop(heap)

        answer = []

        while heap:
            answer.append(heapq.heappop(heap)[1])
        
        return answer

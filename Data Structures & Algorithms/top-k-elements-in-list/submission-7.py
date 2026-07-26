import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == k:
            return nums

        count = {}

        for n in nums:
            count[n] = count.get(n, 0) + 1

        heap = []

        for n in count:
            heapq.heappush(heap, (count[n], n))

            if len(heap) > k:
                heapq.heappop(heap)

        result = []

        while heap:
            result.append(heapq.heappop(heap)[1])

        return result
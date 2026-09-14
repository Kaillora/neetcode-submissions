import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        result = []
        count = Counter(nums)

        for num, freq in count.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            else:
                heapq.heappushpop(heap, (freq, num))
        for i in heap:
            result.append(i[1])
        return result

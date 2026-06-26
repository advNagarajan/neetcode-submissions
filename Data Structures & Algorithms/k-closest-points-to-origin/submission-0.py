class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        heapq.heapify(minHeap)
        res = []

        for i in points:
            dist = math.sqrt(
                (i[0]) ** 2 + 
                (i[1]) ** 2
            )

            heapq.heappush(minHeap, (dist, (i[0], i[1])))

        while k:
            res.append(heapq.heappop(minHeap)[1])
            k -= 1
        
        return res


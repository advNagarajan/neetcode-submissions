class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = [-i for i in nums]
        heapq.heapify(q)
        k -= 1

        while k:
            heapq.heappop(q)
            k -= 1

        return -1 * heapq.heappop(q)
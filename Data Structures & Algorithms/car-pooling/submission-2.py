class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        from_ = []
        to = []
        heapq.heapify(from_)
        heapq.heapify(to)

        for num, f, t in trips:
            heapq.heappush(from_, (f, t, num))

        current = capacity
        while from_:
            f, t, num = heapq.heappop(from_)

            while to and to[0][0] <= f:
                dropoff, passengers = heapq.heappop(to)
                current += passengers

            current -= num

            if current < 0:
                return False

            heapq.heappush(to, (t, num))

        return True
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        order = []
        manifest = []

        for idx, i in enumerate(tasks):
            manifest.append((i[0], i[1], idx))
        
        heapq.heapify(manifest)
        time = manifest[0][0]
        available = []
        heapq.heapify(available)

        for i in range(len(tasks)):      
            if not available and time < manifest[0][0]:
                time = manifest[0][0]

            while manifest and manifest[0][0] <= time:
                e, p, idx = heapq.heappop(manifest)
                heapq.heappush(available, (p, idx))
                if not manifest:
                    break

            p, idx = heapq.heappop(available)
            time += p
            order.append(idx)

        return order
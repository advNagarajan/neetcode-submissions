class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        maxHeap = []
        heapq.heapify(maxHeap)
        res = ""

        for i in freq.items():
            heapq.heappush(maxHeap, (-1 * i[1], i[0]))

        while maxHeap:
            cnt, char = heapq.heappop(maxHeap)
            
            if len(res) > 0 and res[-1] == char:
                if not maxHeap:
                    return ""

                cnt2, char2 = heapq.heappop(maxHeap)
                res += char2
                cnt2 += 1

                if cnt2:
                    heapq.heappush(maxHeap, (cnt2, char2))
            
            else:
                res += char
                cnt += 1

            if cnt:
                heapq.heappush(maxHeap, (cnt, char))
        
        return res
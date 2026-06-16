class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        indeg = {i:0 for i in "".join(words)}
        graph = {c: set() for c in indeg}

        l = 0
        r = l + 1

        while r <= (len(words) - 1):
            first = words[l]
            second = words[r]
            p = 0
            ceiling = min(len(first), len(second))
            while p < ceiling:
                if first[p] != second[p]:
                    if second[p] not in graph[first[p]]:
                        graph[first[p]].add(second[p])
                        indeg[second[p]] += 1
                    break
                p += 1
            
            else:
                if len(words[l]) > len(words[r]):
                    return ""

            l += 1
            r += 1

        q = deque([c for c in indeg if indeg[c] == 0])
        ans = []

        while q:
            ch = q.popleft()
            ans.append(ch)

            for nei in graph[ch]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)

        if len(ans) != len(indeg):
            return ""

        return "".join(ans)


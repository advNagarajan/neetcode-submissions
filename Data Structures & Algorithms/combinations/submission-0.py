class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(arr, start):
            if len(arr) == k:
                res.append(arr[:])
                return

            for i in range(start, n + 1):
                arr.append(i)
                dfs(arr, i + 1)
                arr.pop()

        dfs([], 1)
        return res
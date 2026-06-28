class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(start, arr, cur_sum):
            if cur_sum == target:
                res.append(arr[:])
                return

            if cur_sum > target:
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                arr.append(candidates[i])
                dfs(i + 1, arr, cur_sum + candidates[i])
                arr.pop()

        dfs(0, [], 0)

        return res
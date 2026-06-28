class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(start, arr):
            res.append(arr[:])

            for i in range(start, len(nums)):
                arr.append(nums[i])
                dfs(i + 1, arr)
                arr.pop()

        dfs(0, [])
        return res
            
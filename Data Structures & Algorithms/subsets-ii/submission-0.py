class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(start, arr):
            res.append(arr[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                arr.append(nums[i])
                dfs(i + 1, arr)
                arr.pop()

        dfs(0, [])
        return res
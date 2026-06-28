class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(start, arr, cur_sum):
            if cur_sum == target:
                res.append(arr[:])
                return

            if cur_sum > target:
                return
            
            for i in range(start, len(nums)):
                arr.append(nums[i])
                dfs(i, arr, cur_sum + nums[i])
                arr.pop()

        dfs(0, [], 0)
        return res



class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def dfs(arr):
            if len(arr) == len(nums):
                res.append(arr[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue

                used[i] = True
                arr.append(nums[i])
                
                dfs(arr)

                arr.pop()
                used[i] = False

        dfs([])
        return res
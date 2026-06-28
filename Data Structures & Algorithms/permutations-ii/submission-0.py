class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        used = [False] * len(nums)

        def dfs(arr):
            if len(arr) == len(nums):
                res.append(arr[:])
                return

            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue

                if used[i]:
                    continue
                
                used[i] = True
                arr.append(nums[i])
                
                dfs(arr)

                arr.pop()
                used[i] = False

        dfs([])
        return res


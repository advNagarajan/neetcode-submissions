class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        
        import functools

        @functools.lru_cache(None)
        def dfs(l, r):
            if l > r:
                return 0
            
            res = 0
            for i in range(l, r + 1):
                coins = nums[i] * nums[r + 1] * nums[l - 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                if coins > res:
                    res = coins
            
            return res

        return dfs(1, len(nums) - 2)
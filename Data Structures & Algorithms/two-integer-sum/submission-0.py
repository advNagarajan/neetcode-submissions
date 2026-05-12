class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {n:i for i, n in enumerate(nums)}

        for i, n in enumerate(nums):
            temp = target - n
            if temp in s and i != s[temp]:
                return [i, s[temp]]
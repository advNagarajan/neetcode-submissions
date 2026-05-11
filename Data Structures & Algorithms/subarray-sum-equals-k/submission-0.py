class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefSum = { 0 : 1 }

        for n in nums:
            curSum += n
            diff = curSum - k

            res += prefSum.get(diff, 0)
            prefSum[curSum] = 1 + prefSum.get(curSum, 0)

        return res



            
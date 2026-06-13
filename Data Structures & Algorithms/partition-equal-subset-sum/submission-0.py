class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = set()
        s.add(0)
        temp = sum(nums)
        if temp % 2 != 0:
            return False
        else:
            target = temp / 2

        for i in nums: 
            temp = []

            for j in s:
                temp.append(j+i)

            for j in temp:
                s.add(j)

            if target in s:
                return True

        return False

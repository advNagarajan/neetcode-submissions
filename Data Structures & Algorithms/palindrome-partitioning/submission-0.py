class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans, sol = [], []

        def backtrack(start):
            if start == len(s):
                ans.append(sol[:])

            for end in range(start, len(s)):
                substring = s[start:end+1]
                if substring == substring[::-1]:
                    sol.append(substring)
                    backtrack(end+1)
                    sol.pop()

        backtrack(0)

        return ans
            
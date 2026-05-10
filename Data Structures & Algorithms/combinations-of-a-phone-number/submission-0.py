class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        combo = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }

        if not digits:
            return []

        ans, sol = [], []

        def backtrack(current):
            if len(sol) == len(digits):
                ans.append("".join(sol))
                return

            for i in combo[digits[current]]:
                sol.append(i)
                backtrack(current + 1)
                sol.pop()
        
        backtrack(0)

        return ans
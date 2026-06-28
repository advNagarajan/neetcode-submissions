class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        res = []

        if not digits:
            return []

        def dfs(i, arr):
            if len(arr) == len(digits):
                res.append("".join(arr[:]))
                return
            
            for letter in keypad[digits[i]]:
                arr.append(letter)
                dfs(i + 1, arr)
                arr.pop()

        dfs(0, [])

        return res
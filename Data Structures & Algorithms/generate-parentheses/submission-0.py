class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(openn, closed, arr):
            if len(arr) == 2 * n:
                res.append("".join(arr[:]))
                return
            
            if openn < n:
                arr.append("(")
                dfs(openn + 1, closed, arr)
                arr.pop()

            if closed < openn:
                arr.append(")")
                dfs(openn, closed + 1, arr)
                arr.pop()

        dfs(0, 0, [])
        return res
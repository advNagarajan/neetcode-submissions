class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def isPalindrome(sub):
            return sub == sub[::-1]

        def dfs(start, arr):
            if start == len(s):
                res.append(arr[:])
                return

            for end in range(start, len(s)):
                substring = s[start:end + 1]

                if not isPalindrome(substring):
                    continue

                arr.append(substring)
                dfs(end + 1, arr)
                arr.pop()

        dfs(0, [])
        return res
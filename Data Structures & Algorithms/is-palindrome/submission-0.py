class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = ""
        for i in s:
            if i.isalnum():
                n += i.lower()
        return True if n == n[::-1] else False
class Solution:
    def checkValidString(self, s: str) -> bool:
        paren = []
        star = []

        for i, ch in enumerate(s):
            if ch == "(":
                paren.append(i)
            elif ch == "*":
                star.append(i)
            else:
                if paren:
                    paren.pop()
                elif star:
                    star.pop()
                else:
                    return False

        while paren and star:
            if paren[-1] < star[-1]:
                paren.pop()
                star.pop()
            else:
                return False

        return len(paren) == 0

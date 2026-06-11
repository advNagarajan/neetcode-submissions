class MinStack:

    def __init__(self):
        self.stk = []
        self.min_stk = []
        self.top_idx = -1

    def push(self, val: int) -> None:
        self.stk.append(val)
        
        if not self.min_stk:
            self.min_stk.append(val)
        else:
            self.min_stk.append(min(self.min_stk[self.top_idx], val))

        self.top_idx += 1

    def pop(self) -> None:
        self.stk.pop()
        self.min_stk.pop()
        self.top_idx -= 1

    def top(self) -> int:
        return self.stk[self.top_idx]

    def getMin(self) -> int:
        return self.min_stk[self.top_idx]

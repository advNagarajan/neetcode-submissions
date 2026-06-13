class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        q = deque(piles)
        alice = []
        bob = []

        turn = "alice"
        while q:
            choice = 1 if q[0] > q[-1] else -1

            if choice == 1:
                if turn == "alice":
                    alice.append(q.popleft())
                else:
                    alice.append(q.popleft())
            else:
                if turn == "alice":
                    alice.append(q.pop())
                else:
                    alice.append(q.pop())

        return True if sum(alice) > sum(bob) else False
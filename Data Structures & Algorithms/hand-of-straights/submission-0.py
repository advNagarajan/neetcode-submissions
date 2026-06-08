from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        freq = Counter(hand)

        for card in sorted(freq):
            while freq[card] > 0:
                for nxt in range(card, card + groupSize):
                    if freq[nxt] == 0:
                        return False
                    freq[nxt] -= 1

        return True
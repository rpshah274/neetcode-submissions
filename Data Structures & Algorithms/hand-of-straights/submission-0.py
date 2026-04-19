from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n=len(hand)
        if n%groupSize!=0:
            return False
        freq=Counter(hand)
        for x in sorted(hand):
            while freq[x]>0:
                for n in range(x,x+groupSize):
                    if freq[n]==0:
                        return False
                    freq[n]-=1
        return True

from collections import Counter
from typing import List

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        sorted_keys = sorted(count.keys())
        
        for key in sorted_keys:
            while count[key] > 0:
                for i in range(groupSize):
                    if count[key + i] <= 0:
                        return False
                    count[key + i] -= 1
        
        return True

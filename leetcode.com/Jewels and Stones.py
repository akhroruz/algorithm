# https://leetcode.com/problems/jewels-and-stones/
from collections import Counter


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str, num: int = 0) -> int:
        counter = Counter(stones)
        for i in counter:
            if i in jewels:
                num += counter[i]
        return num

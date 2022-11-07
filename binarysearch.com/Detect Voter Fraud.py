from collections import Counter


class Solution:
    def solve(self, votes):
        return 2 in Counter([i[1] for i in votes]).values()

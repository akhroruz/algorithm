from itertools import zip_longest


class Solution:
    def solve(self, s0, s1):
        s = ''
        for i, v in zip_longest(s0, s1, fillvalue=''):
            s += i + v
        return s
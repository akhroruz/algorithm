from collections import Counter


class Solution:
    def solve(self, nums):
        c, co = 0, Counter(nums)
        for k, v in co.items():
            if k + 1 in co.keys():
                c += co[k]
        return c
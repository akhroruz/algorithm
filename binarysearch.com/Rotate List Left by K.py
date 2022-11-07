from collections import deque


class Solution:
    def solve(self, nums, k):
        d = deque(nums)
        d.rotate(-k)
        return list(d)


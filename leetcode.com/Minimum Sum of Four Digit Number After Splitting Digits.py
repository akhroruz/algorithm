# https://leetcode.com/problems/minimum-sum-of-four-digit-number-after-splitting-digits/
class Solution:
    def minimumSum(self, num: int) -> int:
        num = sorted(str(num))
        return int(num[0] + num[2]) + int(num[1] + num[3])

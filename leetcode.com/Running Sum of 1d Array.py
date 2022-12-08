# https://leetcode.com/problems/running-sum-of-1d-array/
class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        a = []
        for i in range(len(nums)):
            s = 0
            for n in range(i + 1):
                s += nums[n]
            a.append(s)
        return a

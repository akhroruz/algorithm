# https://leetcode.com/problems/shuffle-the-array/
class Solution:
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        a = []
        for i in range(n):
            a.append(nums[i])
            a.append(nums[i + n])
        return a
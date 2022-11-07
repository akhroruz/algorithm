class Solution:
    def solve(self, n):
        return sum(list(map(int, str(bin(n)).replace('0b', ''))))
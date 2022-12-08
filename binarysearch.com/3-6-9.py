class Solution:
    def solve(self, n):
        result = []
        for i in range(1, n + 1):
            if '9' in str(i) or '6' in str(i) or '3' in str(i) or not i % 3 or not i % 6 or not i % 9:
                result.append("clap")
            else:
                result.append(f"{i}")
        return result

class Solution:
    def solve(self, s):
        n = t = s[0]
        for i in range(len(s)):
            if s[i] != t:
                n += s[i]
                t = s[i]
        return n
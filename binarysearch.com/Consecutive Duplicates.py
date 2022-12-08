class Solution:
    def solve(self, s, n='', m=''):
        for i in range(len(s)):
            if s[i] != m:
                n += s[i]
                m = s[i]
        return n

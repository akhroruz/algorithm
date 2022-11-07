class Solution:
    def solve(self, s):
        stack = []
        for i, v in enumerate(s):
            if i > 0 and s[i] == '-' and s[i - 1] == '<':
                stack.pop()
                if stack:
                    stack.pop()
            else:
                stack.append(v)
        return ''.join(stack)

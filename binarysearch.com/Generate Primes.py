def isprime(m):
    if m <= 1:
        return False
    for i in range(2, m):
        if not m % i:
            return False
    return True


class Solution:
    def solve(self, n):
        result = []
        for i in range(2, n + 1):
            if isprime(i):
                result.append(i)
        return result

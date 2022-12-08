class Solution:
    def solve(self, n):
        counter = 0
        if n != 0:
            while n >= 2:
                if not n % 2:
                    n //= 2
                    counter += 1
                else:
                    return False;
            return True;
        else:
            return False
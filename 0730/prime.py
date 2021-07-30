class Solution:
    def solve(self, n):
        primes = set([i for i in range(2, n + 1)])
        for i in range(2, int(sqrt(n)) + 1):
            mul = 2
            while mul * i <= n:
                if mul * i in primes:
                    primes.remove(mul * i)
                mul += 1
        return list(primes)

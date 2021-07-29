class Solution:
    def solve(self, n):
        for i in range(n + 1):
            if i * i == n:
                return True
            if i * i > n:
                return False

# Binary Search would be better
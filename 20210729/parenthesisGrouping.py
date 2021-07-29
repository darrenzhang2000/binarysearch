class Solution:
    def solve(self, s):
        c = 0
        res = []
        i = 0
        j = 0
        while j < len(s):
            if s[j] == '(':
                c += 1
            else:
                c -= 1
            if c == 0:
                res.append(s[i:j+1])
                i = j + 1
            j += 1
            
        return res
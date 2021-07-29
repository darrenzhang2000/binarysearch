class Solution:
    def solve(self, nums):
        saw_one_1 = False
        saw_last_1 = False
        for n in nums:
            if n == 1:
                if not saw_one_1:
                    saw_one_1 = True
                else:
                    if saw_last_1:
                        return False
            else:
                if saw_one_1:
                    saw_last_1 = True
        return True
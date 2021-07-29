class Solution:
    def solve(self, nums):
        indices = sorted([i for i in range(len(nums)) if nums[i] % 2 == 1])
        values = list(reversed(sorted([n for n in nums if n % 2 == 1])))
        for i in range(len(values)):
            idxToInsert = indices[i]
            nums[idxToInsert] = values[i]

        indices = sorted([i for i in range(len(nums)) if nums[i] % 2 == 0])
        values = (sorted([n for n in nums if n % 2 == 0]))
        for i in range(len(values)):
            idxToInsert = indices[i]
            nums[idxToInsert] = values[i]
        return nums
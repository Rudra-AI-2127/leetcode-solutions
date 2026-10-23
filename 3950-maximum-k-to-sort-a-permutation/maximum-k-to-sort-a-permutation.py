class Solution(object):
    def sortPermutation(self, nums):
        n = len(nums)
        if nums == list(range(n)):
            return 0
        k = -1
        for i in range(n):
            if nums[i] != i:
                k &= nums[i] & i
        return k
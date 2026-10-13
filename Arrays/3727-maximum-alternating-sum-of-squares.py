class Solution(object):
    def maxAlternatingSum(self, nums):
        nums.sort(key=lambda x: x * x, reverse=True)
        n = (len(nums) + 1) // 2
        return sum(x * x for x in nums[:n]) - sum(x * x for x in nums[n:])

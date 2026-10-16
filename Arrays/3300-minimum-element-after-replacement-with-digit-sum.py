class Solution(object):
    def minElement(self, nums):
        return min(sum(map(int, str(n))) for n in nums)
        
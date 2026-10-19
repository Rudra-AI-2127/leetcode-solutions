class Solution(object):
    def targetIndices(self, nums, target):
        nums.sort()
        ans = []

        for i in range(len(nums)):
            if nums[i] == target:
                ans.append(i)

        return ans

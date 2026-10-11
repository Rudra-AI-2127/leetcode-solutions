class Solution(object):
    def subsetsWithDup(self, nums):
        nums.sort()
        r = []
        def f(s, a):
            r.append(a[:])
            for i in range(s, len(nums)):
                if i > s and nums[i] == nums[i - 1]:
                    continue
                a.append(nums[i])
                f(i + 1, a)
                a.pop()
        f(0, [])
        return r

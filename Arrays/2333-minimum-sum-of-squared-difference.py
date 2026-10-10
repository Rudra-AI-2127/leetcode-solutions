
class Solution(object):
    def minSumSquareDiff(self, nums1, nums2, k1, k2):
        a = [abs(x - y) for x, y in zip(nums1, nums2)]
        k = k1 + k2
        if sum(a) <= k:
            return 0
        l, r = 0, max(a)
        while l < r:
            m = (l + r) // 2
            if sum(max(0, x - m) for x in a) <= k:
                r = m
            else:
                l = m + 1
        s = sum(min(x, l) ** 2 for x in a)
        t = k - sum(max(0, x - l) for x in a)
        return s - t * (2 * l - 1)
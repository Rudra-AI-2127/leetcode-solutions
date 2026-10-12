class Solution(object):
    def maxSum(self, nums, k):
        from collections import Counter
        c = [0] * 32
        for x in nums:
            for i in range(32):
                c[i] += (x >> i) & 1
        a = []
        for _ in nums:
            x = 0
            for i in range(32):
                if c[i]:
                    x |= 1 << i
                    c[i] -= 1
            a.append(x)
        return sum(x * x for x in sorted(a, reverse=True)[:k]) % (10**9 + 7)
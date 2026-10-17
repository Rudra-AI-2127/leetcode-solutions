class Solution:
    def minSwaps(self, nums):
        def digit_sum(n):
            s = 0
            while n:
                s += n % 10
                n //= 10
            return s

        arr = sorted(nums, key=lambda x: (digit_sum(x), x))
        pos = {v: i for i, v in enumerate(nums)}
        ans = 0

        for i, v in enumerate(arr):
            if nums[i] != v:
                j = pos[v]
                pos[nums[i]] = j
                nums[i], nums[j] = nums[j], nums[i]
                pos[v] = i
                ans += 1

        return ans
class Solution(object):
    def sumCounts(self, nums):
        MOD = 10**9 + 7
        n = len(nums)
        size = 4 * n
        s = [0] * size
        sq = [0] * size
        lazy = [0] * size
        def update(node, start, end, l, r):
            if l <= start and end <= r:
                length = end - start + 1
                v = lazy[node] + 1
                sq[node] = (sq[node] + 2 * s[node] + length) % MOD
                s[node] = (s[node] + length) % MOD
                lazy[node] = v
                return
            mid = (start + end) // 2
            left, right = node * 2, node * 2 + 1
            if lazy[node]:
                v = lazy[node]
                left_len = mid - start + 1
                right_len = end - mid
                sq[left] = (sq[left] + 2 * v * s[left] + v * v * left_len) % MOD
                sq[right] = (sq[right] + 2 * v * s[right] + v * v * right_len) % MOD
                s[left] = (s[left] + v * left_len) % MOD
                s[right] = (s[right] + v * right_len) % MOD
                lazy[left] += v
                lazy[right] += v
                lazy[node] = 0
            if l <= mid:
                update(left, start, mid, l, r)
            if r > mid:
                update(right, mid + 1, end, l, r)
            s[node] = (s[left] + s[right]) % MOD
            sq[node] = (sq[left] + sq[right]) % MOD
        last = {}
        ans = 0
        for i, x in enumerate(nums):
            p = last.get(x, -1) + 1
            last[x] = i
            update(1, 0, n - 1, p, i)
            ans = (ans + sq[1]) % MOD
        return ans

class Solution(object):
    def combine(self, n, k):
        r = []
        def f(s, a):
            if len(a) == k:
                r.append(a[:])
                return
            for i in range(s, n - (k - len(a)) + 2):
                a.append(i)
                f(i + 1, a)
                a.pop()
        f(1, [])
        return r

class Solution(object):
    def minOperations(self, s):
        n = len(s)

        # Already sorted
        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0

        # Cannot sort an unsorted string of length 2
        if n == 2:
            return -1

        mn, mx = min(s), max(s)

        # One operation is enough
        if s[0] == mn or s[-1] == mx:
            return 1

        # Two operations are enough if an extreme character
        # appears in the interior
        for i in range(1, n - 1):
            if s[i] == mn or s[i] == mx:
                return 2

        # Maximum at the beginning and minimum at the end
        return 3

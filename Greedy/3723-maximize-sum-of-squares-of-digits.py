class Solution(object):
    def maxSumOfSquares(self, num, sum):
        if sum > 9 * num:
            return ""

        a, b = divmod(sum, 9)
        return "9" * a + str(b) * (b > 0) + "0" * (num - a - (b > 0))
class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        arr.sort()
        d = arr[1] - arr[0]
        return all(arr[i] - arr[i - 1] == d for i in range(2, len(arr)))
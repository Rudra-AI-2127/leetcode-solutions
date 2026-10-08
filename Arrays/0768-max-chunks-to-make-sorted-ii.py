class Solution(object):
    def maxChunksToSorted(self, arr):
        sorted_arr = sorted(arr)
        count = {}
        chunks = 0
        different = 0
        for i in range(len(arr)):
            x = arr[i]
            count[x] = count.get(x, 0) + 1
            if count[x] == 1:
                different += 1
            elif count[x] == 0:
                different -= 1
            y = sorted_arr[i]
            count[y] = count.get(y, 0) - 1
            if count[y] == 0:
                different -= 1
            elif count[y] == -1:
                different += 1
            if different == 0:
                chunks += 1
        return chunks
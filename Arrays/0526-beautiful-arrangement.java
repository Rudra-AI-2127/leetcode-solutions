class Solution {
    public int countArrangement(int n) {
        boolean[] used = new boolean[n + 1];
        return backtrack(1, n, used);
    }
    private int backtrack(int index, int n, boolean[] used) {
        if (index > n) {
            return 1;
        }
        int count = 0;
        for (int num = 1; num <= n; num++) {
            if (!used[num] &&
                (num % index == 0 || index % num == 0)) {
                used[num] = true;
                count += backtrack(index + 1, n, used);
                used[num] = false;
            }
        }
        return count;
    }
}




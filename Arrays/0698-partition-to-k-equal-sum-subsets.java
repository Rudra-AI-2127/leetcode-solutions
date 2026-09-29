class Solution {
    public boolean canPartitionKSubsets(int[] nums, int k) {
        int total = 0;
        for (int num : nums) {
            total += num;
        }
        if (total % k != 0) {
            return false;
        }
        int target = total / k;
        Arrays.sort(nums);
        if (nums[nums.length - 1] > target) {
            return false;
        }
        boolean[] used = new boolean[nums.length];
        return backtrack(nums, used, k, 0, target);
    }
    private boolean backtrack(
        int[] nums,
        boolean[] used,
        int k,
        int currentSum,
        int target
    ) {
        if (k == 1) {
            return true;
        }
        if (currentSum == target) {
            return backtrack(nums, used, k - 1, 0, target);
        }
        for (int i = nums.length - 1; i >= 0; i--) {
            if (used[i]) {
                continue;
            }
            if (currentSum + nums[i] > target) {
                continue;
            }
            used[i] = true;
            if (backtrack(
                    nums,
                    used,
                    k,
                    currentSum + nums[i],
                    target
            )) {
                return true;
            }
            used[i] = false;
            if (currentSum == 0) {
                break;
            }
        }
        return false;
    }
}
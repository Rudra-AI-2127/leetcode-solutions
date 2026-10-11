class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        def backtrack(i, cur, total):
            if total == target:
                res.append(cur[:])
                return
            if total > target or i == len(candidates):
                return
            cur.append(candidates[i])
            backtrack(i, cur, total + candidates[i])
            cur.pop()
            backtrack(i + 1, cur, total)
        backtrack(0, [], 0)
        return res
        
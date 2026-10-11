class Solution:    
    def arrayPairSum(self, nums):        
        return sum(sorted(nums)[::2])
class Solution:
    def hasDuplicate(self, nums):
        if len(set(nums))<len(nums):
            return True
        else:
            return False

class Solution:
    def twoSum(self, nums: List[int], target: int):
        for i in range (len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]+nums[j] == target:
                    return [i,j]
        ##ek array diya nums nam ka jisme integers store honge
        ## or ek target nam ka variable bnana h
        ## do indices lenge.. or dono ka sum target ke equal aayega toh fir wo output array me paste ho jana chahiye
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ##ek array h nums nam ka
        ##uske hr ek element ka multiplication chahiye h.. except the i
        arr=[]
        for num in range(len(nums)):
            product = 1
            for a in range(len(nums)):
                if num!=a:
                    product *= nums[a]
            arr.append(product)
        return arr

            

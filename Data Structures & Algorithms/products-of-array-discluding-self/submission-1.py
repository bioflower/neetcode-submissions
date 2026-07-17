class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        excluded_list = []
        for index, num in enumerate(nums):
            excluded_nums: List[int] = nums[:index] + nums[index+1:]
            product: int = 1
            for num in excluded_nums:
                product *= num
            excluded_list.append(product)
        return excluded_list

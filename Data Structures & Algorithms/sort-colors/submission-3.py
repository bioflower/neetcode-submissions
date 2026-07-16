class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        complete: bool = True
        def pairwise_comparison(nums: List[int]) -> bool:
            swapped: bool = False
            for i in range(len(nums) - 1):
                if nums[i] > nums[i+1]:
                    bigger_num = nums[i]
                    smaller_num = nums[i+1]
                    nums[i+1] = bigger_num
                    nums[i] = smaller_num
                    swapped = True
            return swapped

        while complete:
            complete = pairwise_comparison(nums)


        
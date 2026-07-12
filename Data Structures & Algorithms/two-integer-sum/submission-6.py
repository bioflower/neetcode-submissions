class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            compliment_num: int = target - nums[i]
            if compliment_num in nums:
                compliment_indices = [q for q, item in enumerate(nums) if item == compliment_num]
                for index in compliment_indices:
                    if index > i:
                        return [i, index]
            
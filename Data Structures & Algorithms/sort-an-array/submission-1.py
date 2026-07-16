class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        num_max = max(nums)
        num_min = min(nums)
        output: List[int] = []
        already_checked_index: List[int] = []

        for digit in range(num_min, num_max + 1, 1):
            for index, num in enumerate(nums):
                if digit == num and index not in already_checked_index:
                    output.append(num)
                    already_checked_index.append(index)
        return output
                    
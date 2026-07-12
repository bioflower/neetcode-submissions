class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        existing_nums: List[int] = []
        for i in nums:
            if i not in existing_nums:
                existing_nums.append(i)
            else:
                return True
        return False
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n: int = len(nums)
        add_ans: List[int] = []

        for i in range(n):
            add_ans.append(nums[i])
        
        return nums + add_ans
    
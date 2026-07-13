class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        threshold: int = math.ceil(len(nums)/2)
        nums_dict: Dict[int, int] = dict()
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 1
            else:
                nums_dict[num] += 1
            
            if nums_dict[num] == threshold:
                return num
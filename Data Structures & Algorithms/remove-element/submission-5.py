class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k: int = 0
        cur_index: int = 0
        nums_copy: List[int] = deepcopy(nums)
        for index, num in enumerate(nums_copy):
            if num != val:
                if cur_index != index:
                    nums[cur_index] = num
                cur_index += 1
                k += 1

        return k
            
            
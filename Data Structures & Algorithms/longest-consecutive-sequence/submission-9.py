class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        set_nums: List[int] = sorted(set(nums))

        cur_num: int = set_nums[0]
        cur_sequence_len: int = 1
        longest_sequence_len: int = 1

        for num in set_nums[1:]:
            if num - 1 == cur_num:
                cur_sequence_len += 1
            else:
                if cur_sequence_len > longest_sequence_len:
                    longest_sequence_len = cur_sequence_len
                cur_sequence_len = 1
            cur_num = num
        return max(longest_sequence_len, cur_sequence_len)
            
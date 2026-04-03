class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest_seq = 0

        for n in nums:
            if (n - 1) in hashset:
                continue

            curr_num = n
            curr_seq_len = 0

            while curr_num in hashset:
                curr_seq_len += 1
                curr_num = curr_num + 1
            
            longest_seq = max(longest_seq, curr_seq_len)
        
        return longest_seq

            
        
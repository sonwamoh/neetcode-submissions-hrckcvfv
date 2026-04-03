class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        max_len = 0

        for n in nums:
            
            if (n - 1) in hashset:
                continue
            
            curr_num = n
            curr_len = 0

            while curr_num in hashset:
                curr_len += 1
                curr_num += 1
            
            max_len = max(max_len, curr_len)
        
        return max_len
        
        
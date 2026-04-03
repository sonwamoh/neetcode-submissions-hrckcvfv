class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        curr_sum = 0
        L = 0
        min_len = float('inf')

        for R in range(len(nums)): # TC: O(n), SC: O(1)
            curr_sum += nums[R]

            while curr_sum >= target:
                min_len = min(min_len, R - L + 1)
                curr_sum -= nums[L]
                L += 1
        
        if min_len == float('inf'):
            return 0
        else:
            return min_len
            

        
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = [0] * n
        postfix_sum = [0] * n

        prev = 0
        for i in range(0, n):
            prefix_sum[i] = prev
            prev += nums[i]
        
        prev = 0
        for i in range(n - 1, -1, -1):
            postfix_sum[i] = prev
            prev += nums[i]
        
        for i in range(n):
            if prefix_sum[i] == postfix_sum[i]:
                return i
        
        return -1
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_idx = {} # K: nums, V: idx # SC: O(n)
        for i, n in enumerate(nums):
            diff = target - n 
            if diff in nums_idx: # O(1)
                return [nums_idx[diff], i]
            nums_idx[n] = i
        return []
        
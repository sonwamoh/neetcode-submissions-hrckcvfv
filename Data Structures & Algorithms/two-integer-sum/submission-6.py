class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIdx = {} # K: nums, V: odx of nums

        # O(n), linear scan
        for i, n in enumerate(nums):
            complement = target - n

            if complement in numToIdx: # O(1)
                return [numToIdx[complement], i]
            
            numToIdx[n] = i
        
        return []
            
        
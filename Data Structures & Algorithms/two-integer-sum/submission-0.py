class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
            1. Use hashmap to track complements & its idx
            2. iterate though nums,
                if complement found, return [comp[idx], idx]
                if complement not found, return []
            TC: O(N), to iterate through nums
            SC: O(N), using map to store complements as key, and their idx as val
        """

        complement_to_index = {}

        for i, n in enumerate(nums):
            complement = target - n
        
            if complement in complement_to_index:
                return [complement_to_index[complement], i]

            complement_to_index[n] = i
        
        return []

        
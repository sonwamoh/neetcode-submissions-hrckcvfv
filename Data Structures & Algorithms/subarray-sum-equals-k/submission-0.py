from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_map = {0: 1}
        prefix_sum = 0
        count = 0

        for n in nums:
            prefix_sum += n
            if (prefix_sum - k) in prefix_sum_map:
                count += prefix_sum_map[prefix_sum - k]
            prefix_sum_map[prefix_sum]  = prefix_sum_map.get(prefix_sum, 0) + 1
        
        return count
        
       
        
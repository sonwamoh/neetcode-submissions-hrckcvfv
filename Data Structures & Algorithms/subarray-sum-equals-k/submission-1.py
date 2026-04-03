from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_map = {0: 1}
        prefix_sum = 0
        count = 0

        for n in nums:
            prefix_sum += n
            diff = prefix_sum - k
            count += prefix_sum_map.get(diff, 0)
            prefix_sum_map[prefix_sum]  = prefix_sum_map.get(prefix_sum, 0) + 1
        
        return count
        
       
        
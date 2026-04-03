class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_idx = []

        for i, n in enumerate(nums):
            nums_idx.append([n, i])
        
        nums_idx.sort(key=lambda x: x[0])
        nums = nums_idx

        left, right = 0, len(nums) - 1
        while left < right:
            curr_sum = nums[left][0] + nums[right][0]

            if curr_sum < target: 
                left += 1
            elif curr_sum > target:
                right -= 1
            else:
                return [min(nums[left][1], nums[right][1]), 
                max(nums[left][1], nums[right][1])]
        return []




        
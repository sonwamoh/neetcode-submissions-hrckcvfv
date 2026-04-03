class Solution:
    def helper(self, nums) -> int:
        house_0, house_1 = 0, 0

        for num in nums:
            curr_house = max(house_0 + num, house_1)
            house_0 = house_1
            house_1 = curr_house 
        return curr_house

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
    
        
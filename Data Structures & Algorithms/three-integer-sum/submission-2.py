class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # TC: O(nlogn)
        res = [] # SC: O(n)

        for i, n in enumerate(nums):
            if n > 0:
                continue
            if i > 0 and n == nums[i - 1]:
                continue 
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                target = n + nums[left] + nums[right]

                if target < 0:
                    left += 1
                elif target > 0:
                    right -= 1
                else:
                    res.append([n, nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

               
        
        return res

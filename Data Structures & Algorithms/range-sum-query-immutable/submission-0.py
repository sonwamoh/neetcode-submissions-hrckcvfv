class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = []
        curr_sum = 0
        for n in nums:
            curr_sum += n
            self.prefix_sum.append(curr_sum)

    def sumRange(self, left: int, right: int) -> int:
        prefix_sum_right = self.prefix_sum[right]
        prefix_sum_left = self.prefix_sum[left - 1] if left > 0 else 0
        return prefix_sum_right - prefix_sum_left
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
class Solution:
    def climbStairs(self, n: int) -> int:
        """
        step 1 : 1 = 1 way
        step 2: 1 + 1, or 2 way
        step 3: step 2 way + step 1 way = 2 + 1 = 3 way
        step 4: step 3 + step 2 = 3 + 2 = 5 way
        step 5: step 4 + step 3 = 5 + 3 = 8 ways
        """
        curr, prev = 1, 1 # confused
        for i in range(1, n):
            tmp = curr
            curr += prev
            prev = tmp
        return curr
        
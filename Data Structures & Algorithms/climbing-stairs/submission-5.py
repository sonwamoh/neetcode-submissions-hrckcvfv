class Solution:
    def climbStairs(self, n: int) -> int:
        """
        step 1 : 1 = 1 way
        step 2: 1 + 1, or 2 way
        step 3: step 2 way + step 1 way = 2 + 1 = 3 way
        step 4: step 3 + step 2 = 3 + 2 = 5 way
        step 5: step 4 + step 3 = 5 + 3 = 8 ways
        """
        if n <= 2:
            return n
        dp = [0] * (n + 1) 
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]        
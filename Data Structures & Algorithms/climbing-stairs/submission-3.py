class Solution:
    def climbStairs(self, n: int) -> int:
        """
        step 1 : 1 = 1 way
        step 2: 1 + 1, or 2 way
        step 3: step 2 way + step 1 way = 2 + 1 = 3 way
        step 4: step 3 + step 2 = 3 + 2 = 5 way
        step 5: step 4 + step 3 = 5 + 3 = 8 ways
        """
        memo = {1:1, 2:2}
        def dfs(n):
            if n in memo:
                return memo[n]
            memo[n] = dfs(n - 1) + dfs(n - 2)
            return memo[n]
        return dfs(n)
        
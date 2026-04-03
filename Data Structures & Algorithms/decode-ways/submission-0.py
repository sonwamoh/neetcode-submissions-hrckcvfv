class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [1, 1]

        if s[0] == '0':
            return 0
        
        for idx, num in enumerate(s[1:], 2):
            ways = 0
            if num != "0":
                ways += dp[idx - 1]
            if 10 <= int(s[idx-2] + num) <= 26:
                ways += dp[idx - 2]
            dp.append(ways)
        return dp[-1]

        
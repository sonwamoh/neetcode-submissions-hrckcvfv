class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        0000
        -----
        0001
        -----
        0010
        0011
        -----
        0100
        0101
        0010
        0011
        -----
        1000
        """
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            dp[i] = 1 + dp[i - offset]
        return dp



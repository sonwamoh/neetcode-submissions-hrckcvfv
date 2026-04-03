class Solution:
    def longestPalindrome(self, s: str) -> str:
        maxLen = 0
        resIdx = 0
        n = len(s)

        def helper(l, r, maxLen, resIdx):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxLen:
                    maxLen = r - l + 1
                    resIdx = l
                l -= 1
                r += 1
            return maxLen, resIdx

        for i in range(n):
            maxLen, resIdx = helper(i, i, maxLen, resIdx)
            maxLen, resIdx = helper(i , i + 1, maxLen, resIdx)
        
        return s[resIdx : resIdx + maxLen]


        
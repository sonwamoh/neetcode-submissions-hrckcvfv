class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0

        def helper(l, r, count):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
            return count

        for i in range(n):
            count = helper(i, i, count)
            count = helper(i , i + 1, count)
        
        return count
        
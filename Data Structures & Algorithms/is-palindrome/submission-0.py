class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = []

        for c in s:
            if c.isalnum():
                newStr.append(c.lower())
        
        print(newStr)
        newStr = ''.join(newStr)
        print(newStr)

        left, right = 0, len(newStr) - 1

        while left <= right:
            if newStr[left] != newStr[right]:
                return False
        
            left += 1
            right -= 1

        return True


        
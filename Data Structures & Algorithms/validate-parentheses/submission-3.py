class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {')': '(', '}': '{', ']': '['}
        stack = []

        for ch in s:
            if ch in close_to_open:
                if stack and stack[-1] == close_to_open[ch]:
                    stack.pop()
                else:
                    return False 
            else:
                stack.append(ch)
        
        return not stack
        
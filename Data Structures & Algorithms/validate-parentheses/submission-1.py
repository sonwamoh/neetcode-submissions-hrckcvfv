class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {')':'(', '}':'{', ']':'['}
        bracket_stack = []

        for bracket in s:
            if bracket in bracket_map:
                if bracket_stack and bracket_stack[-1] == bracket_map[bracket]:
                    bracket_stack.pop()
                else: 
                    return False
            else:
                bracket_stack.append(bracket)
        return not bracket_stack

        
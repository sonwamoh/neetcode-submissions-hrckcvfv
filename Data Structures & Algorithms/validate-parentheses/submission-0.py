class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {')':'(', '}':'{', ']':'['}
        bracket_stack = []

        for bracket in s:
            if bracket in bracket_map: # It's a closing bracket
                if bracket_stack: # If there's opening bracket
                    if bracket_stack[-1] == bracket_map[bracket]:
                        bracket_stack.pop()
                    else: # If there's no opening bracket
                        return False
                else:
                    return False
            else:
                bracket_stack.append(bracket)
        return not bracket_stack

        
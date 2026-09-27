class Solution:
    def isValid(self, s: str) -> bool:
        # Quick check: an odd-length string can never be valid
        if len(s) % 2 != 0:
            return False

        # Map closing brackets to their matching opening brackets
        matching_bracket = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in matching_bracket:
                # If top of stack matches the corresponding open bracket, pop it
                if stack and stack[-1] == matching_bracket[char]:
                    stack.pop()
                else:
                    return False
            else:
                # Push opening brackets onto the stack
                stack.append(char)

        # Valid if all opening brackets were matched and popped
        return len(stack) == 0    
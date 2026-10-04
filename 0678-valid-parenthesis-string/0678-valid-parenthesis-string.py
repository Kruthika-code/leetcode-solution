class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0  
# Minimum possible open brackets needed
        high = 0 
# Maximum possible open brackets allowed
        
        for char in s:
            if char == '(':
                low += 1
                high += 1
            elif char == ')':
                low -= 1
                high -= 1
            else:  # char == '*'
                low -= 1   # Treat '*' as ')'
                high += 1  # Treat '*' as '('
            
# If high drops below 0, there are too many ')' brackets
            if high < 0:
                return False
            
# low cannot be negative; reset to 0
            low = max(low, 0)
            
# If low is 0, we can validly match all open brackets
        return low == 0
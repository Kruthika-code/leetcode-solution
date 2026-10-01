class Solution:
    def convert(self, s: str, numRows: int) -> str:
# Base cases where zigzagging is not necessary
        if numRows == 1 or numRows >= len(s):
            return s
        
# Initialize an array of empty strings for each row
        rows = [''] * numRows
        curr_row = 0
        going_down = False
        
        for char in s:
            rows[curr_row] += char
            
# Change direction when reaching top or bottom boundary
            if curr_row == 0 or curr_row == numRows - 1:
                going_down = not going_down
            
# Move to the next row depending on current direction
            curr_row += 1 if going_down else -1
            
        return "".join(rows)
#Complexity
#Time Complexity:O(N) where N is the length of s, since we iterate through the string once.
#Space Complexity:O(N)to store the characters across all rows.
class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        open_needed = 0
        i = 0
        n = len(s)
        
        while i < n:
            if s[i] == '(':
                open_needed += 1
            else:
                # Check for consecutive '))'
                if i + 1 < n and s[i + 1] == ')':
                    i += 1
                else:
                    insertions += 1  # Add missing ')'
                
                # Balance the '))' pair
                if open_needed > 0:
                    open_needed -= 1
                else:
                    insertions += 1  # Add missing '('
            i += 1
            
        insertions += 2 * open_needed
        return insertions